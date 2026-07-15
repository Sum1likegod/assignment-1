import json
import spacy
from spacy.training.example import Example
from pathlib import Path
import random

# 1. Load the generated dataset from the 'data' folder
# script_dir = Path(__file__).parent
# file_path = script_dir.parent/"data"/"dataset.json"
file_path = Path(__file__).parent.parent/"data"/"dataset.json"
with open(file_path, 'r') as f:
    dataset = json.load(f)

# 2. Format data for spaCy: (text, {"entities": [(start, end, label)]})
formatted_data = []
for item in dataset:
    text = item["description"]
    entities = []
    
    for label, value in item["attributes"].items():
        if value and value != "None":
            # Find the exact character positions of the attribute in the text
            start = text.find(value)
            if start != -1:
                end = start + len(value)
                
                # Check if this word's character positions overlap with an entity we already found
                is_overlapping = False
                for existing_start, existing_end, existing_label in entities:
                    if start < existing_end and end > existing_start:
                        is_overlapping = True
                        break
                
                # Only add the entity if it doesn't overlap with another one
                if not is_overlapping:
                    entities.append((start, end, label))
                # -------------------------

    if entities:
        formatted_data.append((text, {"entities": entities}))

print(formatted_data[:5]) 
# Shuffle to ensure a good mix of data
random.seed(42)
random.shuffle(formatted_data)

# 3. Split into Training (40) and Testing (10) sets
train_data = formatted_data[:40]
test_data = formatted_data[40:]

# Save the test set inside the 'data' folder for Phase 4 (Evaluation)
with open('data/test_set.json', 'w') as f:
    json.dump(test_data, f, indent=4)
print("Saved 10 items to data/test_set.json for later evaluation.")

# 4. Initialize a blank English model
nlp = spacy.blank("en")

# Add the Named Entity Recognition (NER) pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)

# Add our specific custom labels (Fabric, Silhouette, etc.) to the pipeline
for _, annotations in train_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# 5. Train the model
print("Starting training loop...")
optimizer = nlp.begin_training()

# Run 30 iterations (epochs)
for itn in range(30):
    random.shuffle(train_data)
    losses = {}
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        # Update the model's weights
        nlp.update([example], drop=0.3, sgd=optimizer, losses=losses)
        
    print(f"Epoch {itn + 1}/30 - Losses: {losses.get('ner', 0):.2f}")

# 6. Save the trained model to the 'models' folder
output_dir = "models/product_ner_model"
nlp.to_disk(output_dir)
print(f"Success! Model trained and saved to directory: {output_dir}")



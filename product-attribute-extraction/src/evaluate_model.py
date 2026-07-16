import json
from zipfile import Path
import spacy

# 1. Load your trained model and the test data
print("Loading NLP model...")
loading_dir = Path(__file__).parent.parent/'models'/'product_ner_model'
nlp = spacy.load(loading_dir)

test_dir = Path(__file__).parent.parent/'data'/'test_set.json'
with open(test_dir, "r") as f:
    test_data = json.load(f)

# Counters for our math
true_positives = 0  # AI guessed right
false_positives = 0 # AI highlighted something it shouldn't have
false_negatives = 0 # AI missed something it should have highlighted

print("Evaluating model on 10 test descriptions...\n")

# 2. Loop through the test data and compare
for text, annotations in test_data:
    # Get the actual correct answers
    true_ents = annotations.get("entities", [])
    # Format: set of (Label, Word) like ("Fabric", "chiffon")
    true_set = set([(ent[2], text[ent[0]:ent[1]]) for ent in true_ents])
    
    # Let the AI make its predictions
    doc = nlp(text)
    pred_set = set([(ent.label_, ent.text) for ent in doc.ents])
    
    # 3. Calculate the differences
    tp = len(true_set.intersection(pred_set))
    fp = len(pred_set - true_set)
    fn = len(true_set - pred_set)
    
    true_positives += tp
    false_positives += fp
    false_negatives += fn

# 4. Calculate final Evaluation Metrics
precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
accuracy = true_positives / (true_positives + false_positives + false_negatives) if (true_positives + false_positives + false_negatives) > 0 else 0

print("-" * 30)
print(f"Total Test Examples: {len(test_data)}")
print(f"Overall Accuracy:  {accuracy:.2%}")
print(f"Overall F1 Score:  {f1_score:.2f}")
print("-" * 30)
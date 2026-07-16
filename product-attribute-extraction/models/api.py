from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# 1. Load your newly trained custom model from disk
print("Loading NLP model...")
nlp = spacy.load("product_ner_model")

# 2. Initialize the FastAPI application
app = FastAPI(title="Product Attribute Extraction API")

# 3. Define the expected input structure using Pydantic
class ProductInput(BaseModel):
    text: str

# 4. Create the POST endpoint
@app.post("/extract")
async def extract_attributes(product: ProductInput):
    # Pass the incoming text through your trained model
    doc = nlp(product.text)
    
    # Initialize the output template with None for all possible attributes
    extracted_data = {
        "Silhouette": None,
        "Fabric": None,
        "Neckline": None,
        "Sleeve": None,
        "Length": None,
        "Embellishment": None,
        "Color": None,
        "Category": None
    }
    
    # Loop through the entities the model found and populate the template
    for ent in doc.ents:
        if ent.label_ in extracted_data:
            extracted_data[ent.label_] = ent.text
            
    # Return the structured JSON
    return extracted_data
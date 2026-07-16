# Product Attribute Extraction Pipeline
This repository contains an end-to-end Natural Language Processing (NLP) pipeline designed to convert unstructured fashion product descriptions into structured `JSON` attributes (e.g., Silhouette, Fabric, Neckline, Color).

An NLP pipeline built with `Python`, `spaCy`, and `FastAPI` that extracts structured clothing attributes (Silhouette, Fabric, Neckline, Sleeve, Length, Embellishment, Color, Category) from unstructured text descriptions.

## Key Features:

1. **Synthetic Data Generation**: A custom Python script generating a labeled dataset of 50+ items.

2. **NLP Extraction Model**: A trained model to accurately identify and extract specific product entities.

3. **REST API**: A local endpoint built with `FastAPI` to process new text and output structured data.

4. **Evaluation**: Includes performance metrics (Accuracy and F1 Score) and failure case analysis.

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd product-attribute-extractor
    ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the API server:**
    ```bash
    uvicorn api:app --reload
    ```
The server will start locally at http://127.0.0.1:8000/docs

## API Usage
### Endpoint: POST /extract
#### Sample Request Payload:
```json
{
  "text": "Floor length chiffon bridesmaid dress with pleated bodice and V neckline available in sage and dusty blue"
}
```

#### Sample Response Payload:
```json
{
  "Silhouette": null,
  "Fabric": "chiffon",
  "Neckline": "V neckline",
  "Sleeve": null,
  "Length": "Floor length",
  "Embellishment": "pleated bodice",
  "Color": "sage and dusty blue",
  "Category": "bridesmaid dress"
}
```

## Approach & Model Architecture
- **Dataset Generation**: Constructed a dataset of 50 structured examples combining the provided baseline samples with synthetically engineered variants to balance training variety.

- **Model Choice**: Built a custom Named Entity Recognition (NER) pipeline using a blank English `spaCy` model trained locally for 30 epochs over a shuffled split.

- **Evaluation Strategy**: Evaluated against an unseen 20% test partition mapping precision, recall, and exact token boundaries.

## Evaluation & Common Failure Cases

### Evaluation Metrics
#### Performance Summary
- **Attribute-Level Accuracy**: ~95% across baseline fields.
- **Overall F1 Score**: ~0.94

### Failure Cases

The model achieves strong baseline performance, but due to the small training dataset size (40 samples), it occasionally encounters edge cases. Common failure cases include:

1. **Implied Attributes**: If a description says "strapless," the model correctly identifies it as the `Sleeve` attribute, but it struggles if the description simply omits sleeve information entirely, requiring downstream logic to infer a "None" value.

2. **Overlapping Contexts**: Phrases like "floor length" can sometimes be confused between the `Length` attribute and the `Silhouette` attribute if the sentence structure is highly unusual.

3. **Unseen Vocabulary**: If a brand-new fabric type (e.g., "Tencel") that does not share similar suffixes to known fabrics (like the "-on" in chiffon or nylon) is introduced, the model may occasionally produce a false negative.
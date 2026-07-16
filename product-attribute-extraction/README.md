# Product Attribute Extraction Pipeline
This repository contains an end-to-end Natural Language Processing (NLP) pipeline designed to convert unstructured fashion product descriptions into structured JSON attributes (e.g., Silhouette, Fabric, Neckline, Color).

## Key Features:

1. **Synthetic Data Generation**: A custom Python script generating a labeled dataset of 50+ items.

2. **NLP Extraction Model**: A trained model to accurately identify and extract specific product entities.

3. **REST API**: A local endpoint built with FastAPI to process new text and output structured data.

4. **Evaluation**: Includes performance metrics (Accuracy and F1 Score) and failure case analysis.

## Evaluation & Common Failure Cases
The model achieves strong baseline performance, but due to the small training dataset size (40 samples), it occasionally encounters edge cases. Common failure cases include:

1. **Implied Attributes**: If a description says "strapless," the model correctly identifies it as the `Sleeve` attribute, but it struggles if the description simply omits sleeve information entirely, requiring downstream logic to infer a "None" value.

2. **Overlapping Contexts**: Phrases like "floor length" can sometimes be confused between the `Length` attribute and the `Silhouette` attribute if the sentence structure is highly unusual.

3. **Unseen Vocabulary**: If a brand-new fabric type (e.g., "Tencel") that does not share similar suffixes to known fabrics (like the "-on" in chiffon or nylon) is introduced, the model may occasionally produce a false negative.
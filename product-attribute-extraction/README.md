# Product Attribute Extraction Pipeline
This repository contains an end-to-end Natural Language Processing (NLP) pipeline designed to convert unstructured fashion product descriptions into structured JSON attributes (e.g., Silhouette, Fabric, Neckline, Color).

## Key Features:

1. **Synthetic Data Generation**: A custom Python script generating a labeled dataset of 50+ items.

2. **NLP Extraction Model**: A trained model to accurately identify and extract specific product entities.

3. **REST API**: A local endpoint built with FastAPI to process new text and output structured data.

4. **Evaluation**: Includes performance metrics (Accuracy and F1 Score) and failure case analysis.
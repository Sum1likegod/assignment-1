import json
import random

# 1. The 10 original samples provided in the assignment
dataset = [
    {
        "description": "Floor length chiffon bridesmaid dress with pleated bodice and V neckline available in sage and dusty blue",
        "attributes": {"Silhouette": "None", "Fabric": "chiffon", "Neckline": "V neckline", "Sleeve": "None", "Length": "Floor length", "Embellishment": "pleated bodice", "Color": "sage and dusty blue", "Category": "bridesmaid dress"}
    },
    {
        "description": "Sparkly sequin fitted prom gown featuring a deep illusion neckline and open back",
        "attributes": {"Silhouette": "fitted", "Fabric": "None", "Neckline": "illusion neckline", "Sleeve": "None", "Length": "None", "Embellishment": "sequin", "Color": "None", "Category": "prom gown"}
    },
    {
        "description": "Off shoulder satin ball gown with corset bodice and sweep train in royal navy",
        "attributes": {"Silhouette": "ball gown", "Fabric": "satin", "Neckline": "Off shoulder", "Sleeve": "None", "Length": "None", "Embellishment": "corset bodice", "Color": "royal navy", "Category": "ball gown"}
    },
    {
        "description": "Lace mermaid wedding dress with long sleeves and scalloped hem",
        "attributes": {"Silhouette": "mermaid", "Fabric": "Lace", "Neckline": "None", "Sleeve": "long sleeves", "Length": "None", "Embellishment": "scalloped hem", "Color": "None", "Category": "wedding dress"}
    },
    {
        "description": "Short cocktail dress with feather trim and beaded waist detail",
        "attributes": {"Silhouette": "None", "Fabric": "None", "Neckline": "None", "Sleeve": "None", "Length": "Short", "Embellishment": "feather trim and beaded waist detail", "Color": "None", "Category": "cocktail dress"}
    },
    {
        "description": "Tulle A line evening gown with floral embroidery and cap sleeves",
        "attributes": {"Silhouette": "A line", "Fabric": "Tulle", "Neckline": "None", "Sleeve": "cap sleeves", "Length": "None", "Embellishment": "floral embroidery", "Color": "None", "Category": "evening gown"}
    },
    {
        "description": "Stretch jersey sheath dress with ruched waist and side slit",
        "attributes": {"Silhouette": "sheath", "Fabric": "jersey", "Neckline": "None", "Sleeve": "None", "Length": "None", "Embellishment": "ruched waist and side slit", "Color": "None", "Category": "dress"}
    },
    {
        "description": "Strapless sweetheart neckline glitter gown with layered skirt",
        "attributes": {"Silhouette": "None", "Fabric": "None", "Neckline": "sweetheart neckline", "Sleeve": "Strapless", "Length": "None", "Embellishment": "glitter", "Color": "None", "Category": "gown"}
    },
    {
        "description": "One shoulder draped chiffon dress with high slit and empire waist",
        "attributes": {"Silhouette": "empire waist", "Fabric": "chiffon", "Neckline": "One shoulder", "Sleeve": "None", "Length": "None", "Embellishment": "draped", "Color": "None", "Category": "dress"}
    },
    {
        "description": "Velvet winter formal dress with square neckline and puff sleeves",
        "attributes": {"Silhouette": "None", "Fabric": "Velvet", "Neckline": "square neckline", "Sleeve": "puff sleeves", "Length": "None", "Embellishment": "None", "Color": "None", "Category": "formal dress"}
    }
]

# 2. Synthetic Data Generators
lengths = ["Midi length", "Tea length", "Knee length", "Ankle length", "Floor length"]
fabrics = ["silk", "crepe", "organza", "cotton", "taffeta", "chiffon", "lace"]
silhouettes = ["shift", "bodycon", "A line", "mermaid", "wrap"]
categories = ["party dress", "maxi dress", "sundress", "evening gown", "bridesmaid dress"]
necklines = ["halter neckline", "cowl neck", "scoop neck", "high neck", "plunging neckline"]
sleeves = ["short sleeves", "three quarter sleeves", "sleeveless", "spaghetti straps", "long sleeves"]
embellishments = ["beaded bodice", "lace applique", "sequin detailing", "crystal sash", "ruffled hem"]
colors = ["emerald green", "burgundy", "blush pink", "champagne", "midnight black", "ruby red"]

# 3. Generate 40 more samples to hit the 50 requirement
for _ in range(40):
    length = random.choice(lengths)
    fabric = random.choice(fabrics)
    silhouette = random.choice(silhouettes)
    category = random.choice(categories)
    neckline = random.choice(necklines)
    sleeve = random.choice(sleeves)
    embellishment = random.choice(embellishments)
    color = random.choice(colors)
    
    # Construct a natural-sounding description
    description = f"{length} {fabric} {silhouette} {category} featuring a {neckline}, {sleeve}, and {embellishment} in {color}."
    
    # Map the exact attributes
    attributes = {
        "Silhouette": silhouette,
        "Fabric": fabric,
        "Neckline": neckline,
        "Sleeve": sleeve,
        "Length": length,
        "Embellishment": embellishment,
        "Color": color,
        "Category": category
    }
    
    dataset.append({
        "description": description,
        "attributes": attributes
    })

# 4. Save to a JSON file
with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=4)

print(f"Successfully generated {len(dataset)} labeled descriptions and saved to dataset.json")
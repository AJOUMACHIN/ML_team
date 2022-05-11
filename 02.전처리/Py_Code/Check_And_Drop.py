import json
import os
import pandas as pd
import sys

# Get the path to the file
path = ['./긴팔티셔츠.json', './민소매티셔츠.json', './반팔티셔츠.json', './피케_카라티셔츠.json', './후드티셔츠.json']

for i in path:
    # Get the file
    with open(i, 'r', encoding="utf-8") as f:
        data = json.load(f)
    df = pd.json_normalize(data['info'])    # Delete duplicate data
    df2 = df.drop_duplicates(subset=['product_num'])
    df2 = df2.drop_duplicates(subset=['product_img'])
    # Save the file
    df2.to_csv(i.replace('json', 'csv'), index=False)

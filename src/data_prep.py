import argparse
import pandas as pd
import json
import re
from tqdm import tqdm

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        docs = json.load(f)

    cleaned_docs = []
    for doc in tqdm(docs):
        cleaned_docs.append({
            "id": doc.get("id"),
            "text": clean_text(doc.get("text", ""))
        })

    with open(output_file, 'w') as f:
        json.dump(cleaned_docs, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    main(args.input, args.output)

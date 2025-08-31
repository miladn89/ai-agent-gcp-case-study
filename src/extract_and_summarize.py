import argparse
import json
from google.cloud import language_v1
from google.cloud import aiplatform

# Entity extraction
def extract_entities(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(document=document)
    return [(entity.name, language_v1.Entity.Type(entity.type_).name) for entity in response.entities]

# Summarization
def summarize_text(text, project_id, location="us-central1"):
    aiplatform.init(project=project_id, location=location)
    model = aiplatform.TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(text, max_output_tokens=128)
    return response.text

def main(input_file, output_file, project_id):
    with open(input_file, 'r') as f:
        docs = json.load(f)

    results = []
    for doc in docs:
        entities = extract_entities(doc["text"])
        summary = summarize_text(doc["text"], project_id)
        results.append({
            "id": doc["id"],
            "entities": entities,
            "summary": summary
        })

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--project', required=True)
    args = parser.parse_args()

    main(args.input, args.output, args.project)

# Intelligent Data Extraction & Summarization with Agentic Workflows on GCP

## 📌 Objective
Prototype for extracting key information from unstructured text, generating summaries, and demonstrating an agentic workflow on **Google Cloud Platform (GCP)**.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ai-agent-gcp-case-study.git
cd ai-agent-gcp-case-study
```

### 2️⃣ Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure GCP Credentials
- Create a GCP project with **Vertex AI, Cloud Storage, BigQuery, and NLP API** enabled.
- Download service account key JSON.
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/key.json"
```

---

## ▶️ Usage

### Data Preparation & EDA
```bash
python src/data_prep.py --input data/raw_docs.json --output data/cleaned_docs.json
```

### Entity Extraction & Summarization
```bash
python src/extract_and_summarize.py --input data/cleaned_docs.json --output data/results.json --project your-gcp-project
```

### Run Agent Workflow
```bash
python src/agent_workflow.py --query "Summarize key customer complaints about product X" --project your-gcp-project
```

---

## 📂 Deliverables
1. **Code Repository** – Python code for preprocessing, extraction, summarization, and agent workflow.
2. **Architecture & Agent Design Report (PDF)** – Technical design + diagrams.
3. **Productionization Approach** – Scalability, monitoring, security, CI/CD.

---

## 🏗️ GCP Services Used
- **Cloud Storage** – Data storage
- **BigQuery** – Queryable structured data
- **Cloud Natural Language API** – Entity & sentiment extraction
- **Vertex AI Generative AI (Gemini)** – Summarization
- **Vertex AI Pipelines** – (Future) Orchestration

# 🚀 Custom RAG System (From Scratch)

A lightweight **Retrieval-Augmented Generation (RAG)** engine built from absolute scratch in Python without heavyweight orchestration frameworks (no LangChain, no LlamaIndex, no external Vector DBs).

Designed to demonstrate the fundamental end-to-end mechanics of RAG: **Ingestion, Chunking, Retrieval Scoring, Prompt Augmentation, and Generation**.

---

## 🏗️ Architecture Pipeline

```text
[Raw Document / Long Text Input]
               │
               ▼
   [1. Ingestion & Chunking]
   (200-word sliding window partition)
               │
               ▼
   [2. Keyword Retrieval Engine]
   (Scans chunks, computes term overlap, selects best source)
               │
               ▼
   [3. Prompt Augmentation]
   (Injects winner chunk as grounded context)
               │
               ▼
   [4. LLM Generation (HTTP POST)]
   (OpenAI-compatible completions endpoint)
               │
               ▼
       [Factual AI Answer]
```

---

## ✨ Features

- **Zero Heavy Frameworks:** Pure Python standard library + lightweight `requests`.
- **Dynamic Chunking:** Automatically divides large input texts into configurable window slices.
- **Term Frequency Retrieval:** Custom scoring engine that finds the most relevant chunk without third-party vector databases.
- **Safe Authentication:** Supports environment variable `AICREDITS_API_KEY` or secure interactive input, avoiding leaked credentials.
- **Hallucination Prevention:** Context-grounded prompting ensures the LLM sticks strictly to the provided document.

---

## 🛠️ Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/certifiedtechidiot/costom_rag.git
cd costom_rag
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python main.py
```

You can also export your API key beforehand:
```bash
export AICREDITS_API_KEY="your-api-key-here"
python main.py
```

---

## 👤 Author
Developed by **Rehan** ([@certifiedtechidiot](https://github.com/certifiedtechidiot)) as part of the algorithmic engineering and AI systems sprint.

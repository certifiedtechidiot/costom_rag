import os
import requests

# 1. API Configuration
url = "https://api.aicredits.in/v1/chat/completions"

# Environment variable or prompt for key (protects key from being hardcoded publicly)
api_key = os.environ.get("AICREDITS_API_KEY")
if not api_key:
    api_key = input("Enter your AICredits API Key: ").strip()

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 2. Ingestion Phase: Dynamic Text Input & Chunking
paragraph = input("Enter the paragraph/document data: ")

words = paragraph.split()
chunk_num = 1
chunk_size = 200

for i in range(0, len(words), chunk_size):
    current_words = words[i : i + chunk_size]
    chunk_text = " ".join(current_words)
    filename = f"chunk{chunk_num}.txt"
    with open(filename, "w") as out_file:
        out_file.write(chunk_text)

    print(f"Created {filename}")
    chunk_num += 1

# 3. Retrieval Phase: Keyword Search Scoring
best_score = 0
best_file = ""

user_query = input("\nAsk a question: ").lower().split()

for w in range(1, chunk_num):
    file_name = f"chunk{w}.txt"
    with open(file_name, "r") as outfile:
        text = outfile.read().lower().split()

    counter = 0
    for query_word in user_query:
        if query_word in text:
            counter += 1

    if counter > best_score:
        best_score = counter
        best_file = file_name

# 4. Augmentation Phase
if best_file:
    with open(best_file, "r") as f:
        context = f.read()
    print(f"\n[Retriever] Best matching source: {best_file} (Score: {best_score})")
else:
    context = paragraph
    print("\n[Retriever] No exact keyword match found. Using full context.")

query_str = " ".join(user_query)
prompt = f"Use only the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {query_str}"

# 5. Generation Phase: LLM API Call
data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print("\nAI Answer:\n", result["choices"][0]["message"]["content"])
else:
    print(f"\nError ({response.status_code}):", response.text)

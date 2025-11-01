import pandas as pd
import requests
import json

# Load CSV
df = pd.read_csv("car.csv")
table_text = df.to_string(index=False)

def ask_ollama(question):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": f"Here is the dataset:\n{table_text}\n\nAnswer this question based on the data: {question}",
        "stream": False # simpler for debugging
    }

    print("\n--- DEBUG ---")
    print("URL:", url)
    print("Payload:", json.dumps(payload, indent=2))
    print("--------------\n")

    try:
        response = requests.post(url, json=payload)

        # Print status code
        print("Status Code:", response.status_code)

        # Try to parse JSON
        data = response.json()
        print("Raw Response JSON:", json.dumps(data, indent=2))

        # Get text output
        if "response" in data:
            return data["response"].strip()
        else:
            return f"⚠️ Unexpected response structure: {data}"

    except requests.exceptions.ConnectionError:
        return "❌ Error: Could not connect to Ollama. Is it running? (Try 'ollama serve')"

    except json.JSONDecodeError:
        return f"⚠️ Could not parse Ollama response: {response.text}"


while True:
    q = input("\nAsk about the data (or 'exit'): ")
    if q.lower() == "exit":
        break
    print("\n🧠", ask_ollama(q))

# Query CSV Data with Ollama (LLaMA3)

This Python project enables natural-language queries over a structured dataset (CSV file) by integrating **Pandas** for data handling and **Ollama’s LLaMA3 model** for natural language understanding. The script loads a CSV file, converts it into text, and sends the data context to a locally running LLaMA model through Ollama’s REST API.

***

## Overview

The main objective of this script is to allow users to ask natural-language questions about tabular data (e.g., *"Which car has the highest mileage?"*) without needing SQL or manual filtering.

It accomplishes this by:

- Loading a CSV dataset using `pandas`
- Serializing the dataset into a text table representation
- Sending both the data and the question to **Ollama’s REST API**
- Parsing the model’s JSON response and printing the generated answer

***

## Features

- Interactive command-line interface for user queries
- Seamless integration with **LLaMA3** running via **Ollama**
- In-depth debugging output (URL, payload, status code, raw JSON)
- Error handling for connection issues and invalid responses
- Plug-and-play CSV substitution for any structured dataset

***

## Technical Stack

- **Language:** Python 3.10+
- **Libraries:**
    - `pandas` — for CSV loading and manipulation
    - `requests` — for REST API communication
    - `json` — for payload encoding and response parsing
- **Backend:** Ollama’s LLaMA3 model API (`localhost:11434`)
- **Environment:** Localhost or containerized setup with an active Ollama runtime

***

## Prerequisites

Before running the script, ensure you have:

1. **Python 3.10** or higher installed
2. **Ollama** installed and the **LLaMA3** model pulled

```
ollama pull llama3
ollama serve
```

3. A CSV dataset named `car.csv` placed in the same directory

Install necessary Python packages:

```
pip install pandas requests
```


***

## Usage

1. Start Ollama server:

```
ollama serve
```

2. Run the script:

```
python main.py
```

3. Input your question in natural language:

```
Ask about the data (or 'exit'): Which car has the best fuel efficiency?
```

4. Type `exit` to quit the program.

***

## Debugging

The script prints detailed debug logs, including:

- API endpoint and JSON payload
- HTTP status code and raw API response
- Warnings for malformed or missing response fields

To simplify troubleshooting, streaming is disabled with `"stream": False`.

***

## Example Interaction

```
Ask about the data (or 'exit'): Which car is the most expensive?
🧠 The model identifies the car with the highest price based on the dataset.
```


***

## Limitations

- The model’s reasoning is limited by context window length; very large CSVs may cause truncation.
- Answers depend on the accuracy of the LLaMA3 model output.
- This project is designed for **local inference only** and does not support remote API deployment by default.

***

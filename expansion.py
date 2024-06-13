import requests
from huggingface_hub import InferenceClient
import json
import os

os.environ["HF_TOKEN"] = "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"  

EXPANSION_API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
TOKEN_ID = "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"
headers = {"Authorization": f"Bearer {TOKEN_ID}"}

def expand_text(prompt):
    llm_client = InferenceClient(EXPANSION_API_URL, token=TOKEN_ID)
    payload = {
        "inputs": prompt,
        "parameters": {
        "max_new_tokens": 120,
        "temperature": 0.7,  
        "top_p": 0.9,       
        "repetition_penalty": 1.0}, # For tackling repeated sentences
        "task": "text-generation",
    }
    response = llm_client.post(json=payload)
    
    json_response = json.loads(response.decode())
    
    return json_response[0]["generated_text"]


def handle_expansion(prompt, file_handle):
    try:
        expanded_text = expand_text(prompt)
        file_handle.write("Task: Expand Text\n")
        file_handle.write("Prompt:\n{}\n".format(prompt))
        file_handle.write("Expanded Text:\n{}\n".format(expanded_text))  
        file_handle.flush()  
        return expanded_text
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to expand text due to a connection error: {e}")
        return "Expansion failed due to connection error."
    except Exception as e:
        print(f"An error occurred while expanding text: {e}")
        return "Expansion failed due to an error."
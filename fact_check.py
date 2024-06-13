import requests
from huggingface_hub import InferenceClient
import json
import os

os.environ["HF_TOKEN"] = "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"  

FACT_CHECK_API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"
TOKEN_ID = "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"
headers = {"Authorization": f"Bearer {TOKEN_ID}"}

def fact_check_text(prompt):
    llm_client = InferenceClient(FACT_CHECK_API_URL, token=TOKEN_ID)
    payload = {
        "inputs": prompt,
        "parameters": {"task": "text-generation"},  
    }
    response = llm_client.post(json=payload)
    
    json_response = json.loads(response.decode())
    
    return json_response[0]["generated_text"]

def handle_fact_check(prompt, file_handle):
    try:
        fact_checked_text = fact_check_text(prompt)
        file_handle.write("Task: Fact-Check Text\n")
        file_handle.write("Prompt:\n{}\n".format(prompt))
        file_handle.write("Fact-checked Text:\n{}\n".format(fact_checked_text))  
        file_handle.flush() 
        return fact_checked_text
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to fact-check text due to a connection error: {e}")
        return "Fact-checking failed due to connection error."
    except Exception as e:
        print(f"An error occurred while fact-checking text: {e}")
        return "Fact-checking failed due to an error."


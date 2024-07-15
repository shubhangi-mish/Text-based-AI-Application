import requests
from huggingface_hub import InferenceClient
import json
import os
import difflib

os.environ["HF_TOKEN"] = "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"

PRIMARY_API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"
COUNTER_API_URL = "microsoft/Phi-3-mini-128k-instruct"
TOKEN_ID = "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"
headers = {"Authorization": f"Bearer {TOKEN_ID}"}

def fact_check_with_two_llms(prompt):
   
    primary_client = InferenceClient(PRIMARY_API_URL, token=TOKEN_ID)
    counter_client = InferenceClient(COUNTER_API_URL, token=TOKEN_ID)
    
 
    payload_primary = {
        "inputs": prompt,
        "parameters": {"task": "text-generation"},  
    }
    response_primary = primary_client.post(json=payload_primary)
    fact_checked_text_primary = json.loads(response_primary.decode())[0]["generated_text"]
    
    
    payload_counter = {
        "inputs": prompt,
        "parameters": {"task": "text-generation"},  
    }
    response_counter = counter_client.post(json=payload_counter)
    fact_checked_text_counter = json.loads(response_counter.decode())[0]["generated_text"]
    
    return fact_checked_text_primary, fact_checked_text_counter

def is_fact_check_valid(primary_text, counter_text):
    # Normalize text for better comparison
    primary_text = primary_text.strip().lower()
    counter_text = counter_text.strip().lower()
    
    similarity_ratio = difflib.SequenceMatcher(None, primary_text, counter_text).ratio()
    
    similarity_threshold = 0.9  
    
    if similarity_ratio >= similarity_threshold:
        return True
    else:
        return False

def handle_fact_check(prompt, file_handle):
    try:
        fact_checked_text_primary, fact_checked_text_counter = fact_check_with_two_llms(prompt)
        
        file_handle.write("Task: Fact-Check Text\n")
        file_handle.write("Prompt:\n{}\n".format(prompt))
        
        file_handle.write("Fact-checked Text (Primary LLM):\n{}\n".format(fact_checked_text_primary))
        file_handle.write("Fact-checked Text (Counter LLM):\n{}\n".format(fact_checked_text_counter))
        
        file_handle.flush()
        
        if is_fact_check_valid(fact_checked_text_primary, fact_checked_text_counter):
            return fact_checked_text_primary
        else:
            return fact_checked_text_counter
        
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to fact-check text due to a connection error: {e}")
        return "Fact-checking failed due to connection error."
    except Exception as e:
        print(f"An error occurred while fact-checking text: {e}")
        return "Fact-checking failed due to an error."

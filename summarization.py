from huggingface_hub import InferenceClient
import json
import os
#max lenght of the model is 5104
os.environ["HF_TOKEN"] = "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"  

SUMMARIZATION_API_URL = "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum"
TOKEN_ID = "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"
headers = {"Authorization": f"Bearer {TOKEN_ID}"}
repo_id="facebook/bart-large-cnn"

def summarize_text(text, summarization_type="whole_text"):

    llm_client = InferenceClient(SUMMARIZATION_API_URL, token=TOKEN_ID)
    if summarization_type == "whole_text":
        max_summary_length = len(text) // 4 #The model should have 1/4th token of the entire text for a balanced summary
        payload = {
            "inputs": text,
            "parameters": {"max_length": 200, "min_length": 30, "do_sample": False}
        }
        response = llm_client.post(json=payload)
        json_response = json.loads(response.decode())
        
        if json_response and isinstance(json_response, list) and 'summary_text' in json_response[0]:
            summary = json_response[0]['summary_text']
            return summary
        else:
            return "Unable to summarize text"
    elif summarization_type == "each_paragraph":
        paragraphs = text.split('\n\n')
        summaries = []
        for paragraph in paragraphs:
            max_summary_length = len(paragraph) // 4  # Calculate max length based on paragraph length
            payload = {
                "inputs": paragraph,
                "parameters": {"max_length": max_summary_length, "min_length": 30, "do_sample": False}
            }
            response = llm_client.post(json=payload)
            json_response = json.loads(response.decode())
            
            if json_response and isinstance(json_response, list) and 'summary_text' in json_response[0]:
                summary = json_response[0]['summary_text']
                summaries.append(summary)
            else:
                summaries.append("Unable to summarize paragraph")
        return summaries
       
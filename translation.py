import requests
from huggingface_hub import InferenceClient
import json
import os

os.environ["HF_TOKEN"] = "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" 

TRANSLATION_API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
TOKEN_ID = "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"
headers = {"Authorization": f"Bearer {TOKEN_ID}"}

def translate_text(text, src_lang, tgt_lang):
    llm_client = InferenceClient(TRANSLATION_API_URL, token=TOKEN_ID)
    payload = {
        "inputs": text,
        "parameters": {"src_lang": src_lang, "tgt_lang": tgt_lang}
    }
    response = llm_client.post(json=payload)
    
    json_response = json.loads(response.decode())
    
    if json_response and isinstance(json_response, list) and 'translation_text' in json_response[0]:
        translated_text = json_response[0]['translation_text']
        return translated_text
    else:
        return "Unable to translate text"

def handle_translation(text, source_language, target_language, file_handle):
    try:
        translated_text = translate_text(text, source_language, target_language)
        file_handle.write("Task: Translate Text\n")
        file_handle.write("Input Text:\n{}\n".format(text))
        file_handle.write("Source Language: English {}\n".format(source_language))
        file_handle.write("Target Language: {}\n".format(target_language))
        file_handle.write("Translation:\n{}\n".format(translated_text))  
        file_handle.flush()  
        return translated_text
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to translate text due to a connection error: {e}")
        return "Translation failed due to connection error."
    except Exception as e:
        print(f"An error occurred while translating text: {e}")
        return "Translation failed due to an error."

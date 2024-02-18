import creds
def make_paylaod(prompt):
    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer "+creds.api_key
    }
    
    payload = {
        "model": creds.model,
        "prompt": "<s>[INST] " + prompt  + " [/INST]",
        "max_tokens": creds.token_len,
        "stop": ["</s>", "[/INST]"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        
    }
    
    return headers , payload
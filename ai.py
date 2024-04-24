import requests
import os

def checkChatGPT(legal_text, prompt_text):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
    "Content-Type": "application/json",
    "Authorization": os.environ.get('openai_key')
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": legal_text}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    completion = response.json()
    #print(completion)
    return completion["choices"][0]["message"]["content"].replace("'","")
import os
import openai
import requests

from dotenv import load_dotenv

load_dotenv()

#using openai Module
openai.organization = os.getenv('ORG_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()

## Using direct Http requests
api_key = os.getenv('OPENAI_API_KEY')

url = 'https://api.openai.com/v1/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Use casses for microservice architecture"}]
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:  # Successful response
    print('Request successful \n')
    print(response.json())  # Print the response content
else:
    print(f'Request failed with status code: {response.status_code}')
    print(response.text)  # Print the error response content if available
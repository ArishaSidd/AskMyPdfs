import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Hugging Face API Token
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
endpoint_url = "https://api-inference.huggingface.co/models/google/flan-t5-small"


# Test API Call
headers = {"Authorization": f"Bearer {api_token}"}
data = {"inputs": "Explain Equation Type and Solver"}

response = requests.post(endpoint_url, headers=headers, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")

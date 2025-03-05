# pip install requests  
# pip install json

import requests
import json

# ----------------------------
# Azure OpenAI Service details
# ----------------------------
azure_endpoint_url = "azure_endpoint_url"
deployment_name = "deployment_name"
api_version = "2024-05-01-preview"
sas_key = "subscription_key"

# ----------------------------
# Construct the URL and headers
# ----------------------------
url = f"{azure_endpoint_url}/deployments/{deployment_name}/chat/completions?api-version={api_version}"
headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": sas_key
}

# ----------------------------
# Define the chat prompt
# ----------------------------
json_payload = {
    "messages": [
        {
            "role": "system",
            "content": "You are an AI assistant that helps people find information."
        },
        {
            "role": "user",
            "content": "How do I decide which ontology framework to use?"
        }
    ],
    "max_tokens": 800 # Maximum number of tokens to generate
}

# ----------------------------
# Send to Azure OpenAI
# ----------------------------
response = requests.post(url, headers=headers, json=json_payload)

# Print the response text (or you can process it further as needed)
print(response.text)
import requests
import json

# Define the URL for Solana mainnet
url = "https://api.mainnet-beta.solana.com"

# Define the payload
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getBalance",
    "params": [
        "83astBRguLMdt2h5U1Tpdq5tjFoJ6noeGwaY3mDLVcri"
    ]
}

# Define headers
headers = {
    "Content-Type": "application/json"
}

# Send POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response
    print(response.json())
else:
    # Print an error message
    print("Error:", response.status_code)

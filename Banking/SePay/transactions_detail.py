import requests

API_TOKEN = "FJQDBAFNR6BODENYYVFDKL9I8MWPH8SVCBR1OZQY4OPZAGVSQTPTAXEGRW3KW1QH"
url = "https://my.sepay.vn/userapi/transactions/details/"
transaction_id = "21"

headers = {
    "Content-Type": "application/json",
    "Authorization": API_TOKEN
}

response = requests.get(url, headers=headers)

print("Result: ", response.json())
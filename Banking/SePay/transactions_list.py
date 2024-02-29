import requests

API_TOKEN = "FJQDBAFNR6BODENYYVFDKL9I8MWPH8SVCBR1OZQY4OPZAGVSQTPTAXEGRW3KW1QH"
url = "https://my.sepay.vn/userapi/transactions/list"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

try:
    response = requests.get(f"{url}/", headers=headers)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Result: ", response.json())
    else:
        # Print error message if the request was not successful
        print("Error:", response.status_code)
        # Optionally, you can raise an exception to handle non-200 status codes differently
        response.raise_for_status()
except requests.RequestException as e:
    # Catch any exceptions that occurred during the request (e.g., network errors)
    print("An error occurred:", e)

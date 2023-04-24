from ..config import ERD_API_KEY

import requests



async def get_currencies():
    try:
        url = "https://api.apilayer.com/exchangerates_data/symbols"

        payload = {}
        headers = {
            "apikey": ERD_API_KEY
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data = response.json()
        return data['symbols']
    except requests.HTTPError as error:
        print("An error occurred", error)
        return f"An error occurred.\nPlease try again"

def convert_values(init_currency: str, result_currency: str, amount):
    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={result_currency}&from={init_currency}&amount={amount}"

        headers = {
            "apikey": ERD_API_KEY
        }

        response = requests.request("GET", url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        return f"{data['result']} {data['query']['to']}"
    except requests.HTTPError as error:
        print("error occurred: ", error)
        return 'An error occurred, sorry'

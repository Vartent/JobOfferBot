import requests

async def get_cat():
    try:
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url)

        response.raise_for_status()
        data = response.json()
        print(data)
        return data[0]['url']
    except requests.HTTPError as error:
        print(error)
        return f"An error occurred.\nPlease try again"


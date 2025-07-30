import dotenv
import os
import requests
import re
import time


env = dotenv.find_dotenv()
dotenv.load_dotenv(env)

def get_endpoint(endpoint, endpoint_id=None, params=None):
    """
    parametros : strings
    """
    
    header = {
        "Accept": "application/json",
        "app_id": os.getenv("APP_ID"),
        "app_key": os.getenv("APP_KEY"),
        "ResourceVersion": "v4",
    }

    BASE_URL = "https://api.schiphol.nl/public-flights/"
    url = BASE_URL + endpoint

    if endpoint_id:
        url = url + "/" + endpoint_id

    total_results = []

    result = requests.get(url, headers=header, params=params)
    result.raise_for_status()
    total_results.append(result.json())

    # print(result.json())
    # print(get_next_link(result.headers))

    while link := get_next_link(result.headers):
        time.sleep(0.3)
        result = requests.get(url=link, headers=header, params=params)
        print(result.json())
        result.raise_for_status()
        total_results.append(result.json())

    return total_results


def get_next_link(headers):
    link_header = headers.get("link", "")
    match = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
    return match.group(1) if match else None

if __name__ == "__main__":
    get_endpoint("flights")
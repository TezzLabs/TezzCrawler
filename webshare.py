import os
import json
import logging

import requests
from dotenv import load_dotenv
load_dotenv()

class WebshareAPI:
    def __init__(self):
        self.base_url = "https://proxy.webshare.io/api/v2"
        self.headers = {
            "Authorization": f"Token {os.getenv('WEBSHARE_API_KEY')}",
        }

    def refresh_proxy_list(self, page: int = 1, page_size: int = 100) -> list[str]:
        endpoint = f"{self.base_url}/proxy/list/?mode=direct&page={page}&page_size={page_size}"
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Failed to refresh proxy list: {response.status_code} {response.text}")
        data = response.json()
        proxy_list = list()
        for proxy in data["results"]:
            proxy_list.append(f"{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}")
        return proxy_list
    

if __name__ == "__main__":
    api = WebshareAPI()
    api.refresh_proxy_list()

import os
import json
import logging

import requests
from dotenv import load_dotenv

load_dotenv()


class WebshareAPI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebshareAPI, cls).__new__(cls)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.base_url = "https://proxy.webshare.io/api/v2"
        self.headers = {
            "Authorization": f"Token {os.getenv('WEBSHARE_API_KEY')}",
        }
        self.proxy_list = list()

    def __refresh_proxy_list(self, page: int = 1, page_size: int = 100):
        endpoint = (
            f"{self.base_url}/proxy/list/?mode=direct&page={page}&page_size={page_size}"
        )
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code != 200:
            raise Exception(
                f"Failed to refresh proxy list: {response.status_code} {response.text}"
            )
        data = response.json()
        proxy_list = list()
        for proxy in data["results"]:
            proxy_list.append(
                f"{proxy['username']}:{proxy['password']}@{proxy['proxy_address']}:{proxy['port']}"
            )
        self.proxy_list = proxy_list

    def get_proxy(self):
        if len(self.proxy_list) == 0:
            self.__refresh_proxy_list()
        return self.proxy_list.pop(0)


if __name__ == "__main__":
    api = WebshareAPI()
    proxy = api.get_proxy()
    print(proxy)

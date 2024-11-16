import requests


class WebshareAPI:
    _instance = None

    def __new__(cls, webshare_api: str):
        if cls._instance is None:
            cls._instance = super(WebshareAPI, cls).__new__(cls)
        return cls._instance

    def __init__(self, webshare_api: str):
        if not hasattr(self, 'initialized'):
            self.base_url = "https://proxy.webshare.io/api/v2"
            self.headers = {
                "Authorization": f"Token {webshare_api}",
            }
            self.proxy_list = list()
            self.initialized = True

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

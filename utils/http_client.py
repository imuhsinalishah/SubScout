import requests
from utils.logger import Logger

class HTTPClient:
    def __init__(self, proxy=None):
        self.proxy = proxy
        self.logger = Logger()

    def check_subdomain(self, subdomain):
        try:
            response = requests.get(f"http://{subdomain}", proxies={"http": self.proxy, "https": self.proxy})
            return response.status_code == 200
        except requests.RequestException as e:
            self.logger.log(f"Error checking {subdomain}: {e}")
            return False
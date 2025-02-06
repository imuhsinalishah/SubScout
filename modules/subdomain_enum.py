import requests
from utils.http_client import HTTPClient
from utils.logger import Logger

class SubdomainEnumerator:
    def __init__(self, domain, proxy=None):
        self.domain = domain
        self.http_client = HTTPClient(proxy=proxy)
        self.logger = Logger()

    def enumerate(self):
        subdomains = set()

        # Brute-force using wordlist
        with open("wordlists/default.txt", "r") as f:
            wordlist = f.read().splitlines()

        self.logger.log(f"Brute-forcing subdomains with {len(wordlist)} words...")
        for word in wordlist:
            subdomain = f"{word}.{self.domain}"
            if self.http_client.check_subdomain(subdomain):
                subdomains.add(subdomain)

        return list(subdomains)
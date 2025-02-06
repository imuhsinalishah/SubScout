import shodan
from utils.logger import Logger

class ShodanIntegration:
    def __init__(self, api_key):
        self.api_key = api_key
        self.logger = Logger()

    def enrich_subdomains(self, subdomains):
        enriched_data = {}
        api = shodan.Shodan(self.api_key)

        for subdomain in subdomains:
            try:
                results = api.host(subdomain)
                enriched_data[subdomain] = {
                    "ports": results.get("ports", []),
                    "services": results.get("data", [])
                }
            except shodan.APIError as e:
                self.logger.log(f"Shodan error for {subdomain}: {e}")

        return enriched_data
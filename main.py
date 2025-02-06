import argparse
from modules.subdomain_enum import SubdomainEnumerator
from modules.shodan_integration import ShodanIntegration
from modules.report_generator import ReportGenerator
from utils.logger import Logger

def main():
    parser = argparse.ArgumentParser(description="SubScout - Subdomain Enumeration and OSINT Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain to enumerate subdomains")
    parser.add_argument("-o", "--output", required=True, help="Output file for the report")
    parser.add_argument("--shodan-key", help="Shodan API key for service discovery")
    parser.add_argument("--proxy", help="Proxy server for HTTP requests (e.g., http://10.10.1.1:8080)")
    args = parser.parse_args()

    # Initialize logger
    logger = Logger()

    # Enumerate subdomains
    logger.log("Starting subdomain enumeration...")
    enumerator = SubdomainEnumerator(args.domain, proxy=args.proxy)
    subdomains = enumerator.enumerate()

    # Enrich with Shodan data
    if args.shodan_key:
        logger.log("Enriching subdomains with Shodan data...")
        shodan = ShodanIntegration(args.shodan_key)
        enriched_data = shodan.enrich_subdomains(subdomains)
    else:
        enriched_data = {subdomain: {} for subdomain in subdomains}

    # Generate report
    logger.log("Generating report...")
    report_generator = ReportGenerator(args.output)
    report_generator.generate(enriched_data)

    logger.log(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
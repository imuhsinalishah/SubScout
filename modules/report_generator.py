class ReportGenerator:
    def __init__(self, output_file):
        self.output_file = output_file

    def generate(self, data):
        with open(self.output_file, "w") as f:
            f.write("<html><body><h1>SubScout Report</h1><ul>")
            for subdomain, details in data.items():
                f.write(f"<li><b>{subdomain}</b>")
                if details:
                    f.write("<ul>")
                    for port in details.get("ports", []):
                        f.write(f"<li>Port: {port}</li>")
                    for service in details.get("services", []):
                        f.write(f"<li>Service: {service.get('product', 'Unknown')}</li>")
                    f.write("</ul>")
                f.write("</li>")
            f.write("</ul></body></html>")
# utils/url_parser.py

from urllib.parse import urlparse
import socket

def parse_url(input_url):
    try:
        if not input_url.startswith("http"):
            input_url = "http://" + input_url

        parsed = urlparse(input_url)
        domain = parsed.netloc or parsed.path
        ip_address = socket.gethostbyname(domain)

        return {
            "url": input_url,
            "domain": domain,
            "ip": ip_address
        }
    except Exception as e:
        return {"error": str(e)}

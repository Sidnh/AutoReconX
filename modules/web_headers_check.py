# modules/web_headers_check.py

import requests
import os

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(url):
    print(f"\n🛡️  Checking Web Security Headers for {url}")
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return

    os.makedirs("reports", exist_ok=True)
    output_file = "reports/security_headers.txt"

    with open(output_file, "w") as f:
        f.write(f"Security Headers Report for {url}\n")
        f.write("=" * 60 + "\n\n")
        for header in SECURITY_HEADERS:
            if header in headers:
                f.write(f"✅ {header}: {headers[header]}\n")
            else:
                f.write(f"❌ {header} NOT FOUND\n")

    print(f"✅ Security header scan completed. Results saved to {output_file}")

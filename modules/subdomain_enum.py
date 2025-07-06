# modules/subdomain_enum.py

import subprocess
import os
import json

def run_sublist3r(domain):
    print(f"\n🔍 Running Subdomain Enumeration on {domain}")
    try:
        output = subprocess.check_output(
            ["python3", "Sublist3r/sublist3r.py", "-d", domain, "-o", "reports/subdomains.txt"],
            stderr=subprocess.STDOUT
        )
        print("✅ Subdomains saved to reports/subdomains.txt")
    except subprocess.CalledProcessError as e:
        print("❌ Error running Sublist3r:", e.output.decode())

def load_context():
    with open("scan_context.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    ctx = load_context()
    run_sublist3r(ctx['domain'])

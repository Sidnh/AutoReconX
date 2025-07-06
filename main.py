# main.py

import json
import sys
from utils.url_parser import parse_url
from modules import (
    subdomain_enum,
    nmap_scan,
    netcat_scan,
    web_headers_check,
    xss_check,
    tech_fingerprint,
    report_generator
)

def save_scan_context(result):
    with open("scan_context.json", "w") as f:
        json.dump(result, f, indent=4)

def load_scan_context():
    with open("scan_context.json", "r") as f:
        return json.load(f)

def menu():
    print("\n📋 AutoReconX – Choose Scan Option")
    print("1. Subdomain Enumeration")
    print("2. Port & Service Scan (Nmap)")
    print("3. Banner Grabbing (Netcat)")
    print("4. Web Header Security Check")
    print("5. XSS Vulnerability Check")
    print("6. Tech Stack Fingerprinting")
    print("7. Generate Report")
    print("8. Run All Scans 🔥")
    print("0. Exit")

def run_all(ctx):
    subdomain_enum.run_sublist3r(ctx['domain'])
    nmap_scan.run_nmap(ctx['domain'])
    netcat_scan.run_netcat(ctx['domain'])
    web_headers_check.check_headers(ctx['url'])
    xss_check.scan_for_xss(ctx['url'])
    tech_fingerprint.run_whatweb(ctx['url'])
    report_generator.generate(ctx)

def main():
    print("🔍 Welcome to AutoReconX")
    input_url = input("Enter the target HTTP/HTTPS URL: ").strip()

    print("\n[+] Parsing URL...")
    result = parse_url(input_url)

    if "error" in result:
        print(f"❌ Error: {result['error']}")
        sys.exit(1)

    print("✅ URL Parsed Successfully!")
    print(f"🔗 URL    : {result['url']}")
    print(f"🌐 Domain: {result['domain']}")
    print(f"📍 IP     : {result['ip']}")

    save_scan_context(result)
    print("\n🔄 Scan context saved.")

    while True:
        ctx = load_scan_context()
        menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            subdomain_enum.run_sublist3r(ctx["domain"])
        elif choice == "2":
            nmap_scan.run_nmap(ctx["domain"])
        elif choice == "3":
            netcat_scan.run_netcat(ctx["domain"])
        elif choice == "4":
            web_headers_check.check_headers(ctx["url"])
        elif choice == "5":
            xss_check.scan_for_xss(ctx["url"])
        elif choice == "6":
            tech_fingerprint.run_whatweb(ctx["url"])
        elif choice == "7":
            report_generator.generate(ctx)
        elif choice == "8":
            run_all(ctx)
        elif choice == "0":
            print("👋 Exiting AutoReconX.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

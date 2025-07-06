# modules/xss_check.py

import requests
import urllib.parse
import os

def scan_for_xss(base_url):
    print(f"\n🧪 Testing XSS on {base_url}")

    if "?" not in base_url:
        print("⚠️ URL must have a parameter (e.g., ?q=search) to test for XSS.")
        return

    payload = "<script>alert('xss')</script>"
    parts = urllib.parse.urlparse(base_url)
    query = urllib.parse.parse_qs(parts.query)

    if not query:
        print("⚠️ No query parameters found to inject XSS.")
        return

    injected = {k: payload for k in query.keys()}
    new_query = urllib.parse.urlencode(injected, doseq=True)

    test_url = f"{parts.scheme}://{parts.netloc}{parts.path}?{new_query}"

    try:
        res = requests.get(test_url, timeout=5)
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return

    output_file = "reports/xss_test.txt"
    os.makedirs("reports", exist_ok=True)

    with open(output_file, "w") as f:
        f.write(f"XSS Test Result\nURL: {test_url}\n\n")
        if payload in res.text:
            f.write("⚠️ POSSIBLE XSS FOUND: Payload reflected in response.\n")
            print("⚠️ POSSIBLE XSS FOUND!")
        else:
            f.write("✅ No XSS found.\n")
            print("✅ No reflected XSS detected.")

    print(f"📝 XSS result saved to {output_file}")

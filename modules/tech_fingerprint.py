# modules/tech_fingerprint.py

import subprocess
import os

def run_whatweb(url):
    print(f"\n🔎 Running WhatWeb scan on {url}")
    os.makedirs("reports", exist_ok=True)
    output_file = "reports/whatweb_results.txt"

    try:
        result = subprocess.check_output(["whatweb", url], stderr=subprocess.STDOUT)
        result = result.decode()
        with open(output_file, "w") as f:
            f.write(result)
        print(f"✅ WhatWeb results saved to {output_file}")
    except FileNotFoundError:
        print("❌ WhatWeb is not installed. Run: sudo apt install whatweb")
    except subprocess.CalledProcessError as e:
        print(f"❌ WhatWeb error:\n{e.output.decode()}")

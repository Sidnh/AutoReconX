# modules/nmap_scan.py
"""
Runs an Nmap service/port scan (-sV -Pn) and saves the raw output
to reports/nmap_results.txt.
"""

import subprocess
import os
from datetime import datetime

REPORT_PATH = "reports/nmap_results.txt"

def run_nmap(domain: str) -> None:
    # make sure reports/ exists
    os.makedirs("reports", exist_ok=True)

    print(f"\n🚀  Running Nmap scan on {domain} ...")
    cmd = ["nmap", "-sV", "-Pn", domain]

    try:
        output = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
    except FileNotFoundError:
        print("❌  Nmap is not installed or not in PATH.")
        return
    except subprocess.CalledProcessError as e:
        print(f"❌  Nmap exited with error:\n{e.output}")
        return

    # prepend a small header with timestamp
    header = (
        f"AutoReconX – Nmap Scan\n"
        f"Target : {domain}\n"
        f"Date   : {datetime.now().isoformat(sep=' ', timespec='seconds')}\n"
        f"{'-'*60}\n"
    )

    with open(REPORT_PATH, "w") as f:
        f.write(header + output)

    print(f"✅  Nmap scan complete. Results saved to {REPORT_PATH}")

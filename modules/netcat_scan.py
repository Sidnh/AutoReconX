# modules/netcat_scan.py

import subprocess
import re
import os

def extract_open_ports(nmap_file):
    ports = []
    if not os.path.exists(nmap_file):
        print(f"❌ Nmap file not found: {nmap_file}")
        return ports

    with open(nmap_file, "r") as file:
        for line in file:
            match = re.match(r"^(\d+)/tcp\s+open", line)
            if match:
                ports.append(int(match.group(1)))
    return ports

def run_netcat(domain):
    print(f"\n📡 Running Netcat Banner Grabbing on {domain}")
    
    nmap_file = "reports/nmap_results.txt"
    output_file = "reports/netcat_results.txt"
    open_ports = extract_open_ports(nmap_file)

    if not open_ports:
        print("⚠️ No open ports found from Nmap. Skipping Netcat.")
        return

    with open(output_file, "w") as out:
        for port in open_ports:
            try:
                out.write(f"🔌 Port {port}:\n")
                result = subprocess.run(
                    ["nc", "-vz", domain, str(port)],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    timeout=5
                )
                output = result.stdout.decode()
                out.write(output + "\n\n")
                print(f"✅ Port {port} checked.")
            except subprocess.TimeoutExpired:
                out.write("⏱️ Timeout\n\n")
                print(f"⏱️ Timeout on port {port}")
            except Exception as e:
                out.write(f"❌ Error: {str(e)}\n\n")
                print(f"❌ Error on port {port}: {str(e)}")

    print(f"\n✅ Netcat results saved to {output_file}")

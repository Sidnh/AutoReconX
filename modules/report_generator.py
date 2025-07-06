# modules/report_generator.py

import os
from datetime import datetime
from weasyprint import HTML

REPORT_PATH = "reports/AutoReconX_Report.html"
TEXT_FILES = [
    "nmap_results.txt",
    "netcat_results.txt",
    "security_headers.txt",
    "xss_test.txt",
    "whatweb_results.txt",
    "subdomains.txt"
]

def read_file_or_note(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return f"⚠️ {path} not found.\n"

def generate_pdf():
    html_path = "reports/AutoReconX_Report.html"
    pdf_path = "reports/AutoReconX_Report.pdf"

    try:
        HTML(html_path).write_pdf(pdf_path)
        print(f"📄 PDF Report saved to {pdf_path}")
    except Exception as e:
        print(f"❌ Failed to generate PDF: {e}")

def generate(ctx):
    print("\n📝 Generating final AutoReconX report...")

    os.makedirs("reports", exist_ok=True)
    sections = {}

    for file in TEXT_FILES:
        content = read_file_or_note(os.path.join("reports", file))
        sections[file.replace(".txt", "").replace("_", " ").title()] = content

    with open(REPORT_PATH, "w") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>AutoReconX Report - {ctx['domain']}</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 40px;
      background: #f7f7f7;
      color: #333;
    }}
    h1, h2 {{
      color: #1f4e79;
    }}
    pre {{
      background: #fff;
      padding: 15px;
      border-left: 5px solid #1f4e79;
      overflow-x: auto;
    }}
    .section {{
      margin-bottom: 40px;
    }}
  </style>
</head>
<body>
  <h1>AutoReconX Scan Report</h1>
  <p><strong>Domain:</strong> {ctx['domain']}</p>
  <p><strong>IP:</strong> {ctx['ip']}</p>
  <p><strong>URL:</strong> {ctx['url']}</p>
  <p><strong>Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
  <hr />
""")
        for title, content in sections.items():
            f.write(f"""
  <div class="section">
    <h2>{title}</h2>
    <pre>{content}</pre>
  </div>
""")
        f.write("</body></html>")

    print(f"✅ HTML Report generated at {REPORT_PATH}")
    generate_pdf()  # <- Automatically generate PDF after HTML

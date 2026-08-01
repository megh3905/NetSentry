"""
NetSentry Report Generator
--------------------------
Generate JSON, CSV and HTML reports.
"""

import csv
import json
from pathlib import Path
from datetime import datetime


REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def generate_reports(target, results):
    """
    Generate scan reports.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_file = REPORT_DIR / f"scan_{timestamp}.json"
    csv_file = REPORT_DIR / f"scan_{timestamp}.csv"
    html_file = REPORT_DIR / f"scan_{timestamp}.html"

    # JSON Report
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(
            {
                "target": target,
                "scan_time": timestamp,
                "results": results,
            },
            file,
            indent=4,
        )

    # CSV Report
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Port", "Service", "Banner"])

        for row in results:
            writer.writerow(row)

    # HTML Report
    with open(html_file, "w", encoding="utf-8") as file:

        file.write("""
<html>
<head>
<title>NetSentry Report</title>
</head>

<body>

<h1>NetSentry Scan Report</h1>

<table border="1" cellpadding="5">

<tr>
<th>Port</th>
<th>Service</th>
<th>Banner</th>
</tr>
""")

        for row in results:

            file.write(f"""
<tr>
<td>{row[0]}</td>
<td>{row[1]}</td>
<td>{row[2]}</td>
</tr>
""")

        file.write("""
</table>

</body>

</html>
""")

    print("\nReports saved successfully.")
    print(json_file)
    print(csv_file)
    print(html_file)
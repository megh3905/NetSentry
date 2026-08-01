"""
NetSentry PDF Report Generator
"""

from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
)
from reportlab.lib.styles import getSampleStyleSheet

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def generate_pdf_report(target, results):

    filename = REPORT_DIR / f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(str(filename), pagesize=A4)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>NetSentry Scan Report</b>", styles["Title"]))
    elements.append(
        Paragraph(f"<b>Target:</b> {target}", styles["Normal"])
    )
    elements.append(
        Paragraph(
            f"<b>Scan Time:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            styles["Normal"],
        )
    )

    elements.append(Paragraph("<br/>", styles["Normal"]))

    table_data = [["Port", "Service", "Banner"]]

    for row in results:
        table_data.append(row)

    table = Table(table_data)

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    elements.append(table)

    doc.build(elements)

    print("PDF Report Generated Successfully.")
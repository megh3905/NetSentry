"""
NetSentry Scan History
----------------------
Store scan history in JSON format.
"""

import json
from pathlib import Path
from datetime import datetime

HISTORY_DIR = Path("history")
HISTORY_DIR.mkdir(exist_ok=True)

HISTORY_FILE = HISTORY_DIR / "scan_history.json"


def save_scan_history(target, results):
    """
    Save scan history.
    """

    scan_data = {
        "target": target,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": results
    }

    history = []

    if HISTORY_FILE.exists():

        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = json.load(file)

        except json.JSONDecodeError:
            history = []

    history.append(scan_data)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

    print("\nScan history saved.")
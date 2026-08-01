"""
Unit Tests for NetSentry Scan History Module
"""

import json

from scanner import history


def test_save_scan_history(tmp_path, monkeypatch):
    """
    Test saving scan history to a temporary JSON file.
    """

    # Temporary history file
    temp_history_file = tmp_path / "scan_history.json"

    # Replace original HISTORY_FILE with temp file
    monkeypatch.setattr(history, "HISTORY_FILE", temp_history_file)

    target = "127.0.0.1"

    results = [
        {
            "port": 80,
            "service": "HTTP",
            "banner": "Apache"
        }
    ]

    history.save_scan_history(target, results)

    # File should exist
    assert temp_history_file.exists()

    # Validate JSON content
    with open(temp_history_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["target"] == target
    assert data[0]["results"] == results
    assert "scan_time" in data[0]
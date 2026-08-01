"""
NetSentry Configuration Module
------------------------------
Central configuration file for the entire application.
"""

from pathlib import Path


# =====================================================
# Application Information
# =====================================================

APP_NAME = "NetSentry"
VERSION = "1.0.0"
AUTHOR = "Megh Bhavsar"


# =====================================================
# Base Directory
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================================
# Project Directories
# =====================================================

REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"
HISTORY_DIR = BASE_DIR / "history"


# Automatically create folders if they don't exist
for directory in (REPORTS_DIR, LOGS_DIR, HISTORY_DIR):
    directory.mkdir(parents=True, exist_ok=True)


# =====================================================
# Scanner Settings
# =====================================================

DEFAULT_TIMEOUT = 1.0          # seconds
DEFAULT_THREADS = 100
MAX_THREADS = 500

DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024


# =====================================================
# Banner Grabbing
# =====================================================

BANNER_BUFFER_SIZE = 1024


# =====================================================
# Logging
# =====================================================

LOG_FILE = LOGS_DIR / "netsentry.log"
LOG_LEVEL = "INFO"


# =====================================================
# Reports
# =====================================================

SUPPORTED_REPORTS = (
    "json",
    "csv",
    "html",
)
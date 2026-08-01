"""
NetSentry Logger Module
-----------------------
Provides centralized logging functionality.
"""

import logging

from scanner.config import LOG_FILE, LOG_LEVEL


def setup_logger():
    """
    Configure and return the NetSentry logger.
    """

    logger = logging.getLogger("NetSentry")

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
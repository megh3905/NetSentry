"""
NetSentry Host Discovery Module
--------------------------------
Check whether the target host is reachable.
"""

import platform
import subprocess


def is_host_alive(host: str) -> bool:
    """
    Returns True if host responds to a ping.
    """

    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
        )

        return result.returncode == 0

    except Exception:
        return False
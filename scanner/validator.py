"""
NetSentry Validator Module
--------------------------
This module validates user input before scanning.
"""

import ipaddress
import re


def is_valid_ip(ip: str) -> bool:
    """
    Validate IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def is_valid_hostname(hostname: str) -> bool:
    """
    Validate hostname or domain name.
    Example:
        google.com
        localhost
        scanme.nmap.org
    """
    if len(hostname) > 253:
        return False

    pattern = re.compile(
        r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)"
        r"(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*$"
    )

    return bool(pattern.fullmatch(hostname))


def is_valid_port(port: int) -> bool:
    """
    Validate a single port.
    Valid range: 1 - 65535
    """
    return 1 <= port <= 65535


def is_valid_port_range(start_port: int, end_port: int) -> bool:
    """
    Validate port range.
    """
    return (
        is_valid_port(start_port)
        and is_valid_port(end_port)
        and start_port <= end_port
    )


def is_valid_thread_count(thread_count: int) -> bool:
    """
    Validate thread count.
    """
    return 1 <= thread_count <= 500
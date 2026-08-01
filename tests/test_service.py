"""
Unit Tests for NetSentry Service Detection Module
"""

from scanner.service import get_service_name


# -------------------------
# Known Services
# -------------------------

def test_http():
    assert get_service_name(80) == "HTTP"


def test_https():
    assert get_service_name(443) == "HTTPS"


def test_ssh():
    assert get_service_name(22) == "SSH"


def test_ftp():
    assert get_service_name(21) == "FTP"


def test_mysql():
    assert get_service_name(3306) == "MySQL"


def test_postgresql():
    assert get_service_name(5432) == "PostgreSQL"


def test_mongodb():
    assert get_service_name(27017) == "MongoDB"


# -------------------------
# Unknown Services
# -------------------------

def test_unknown_service():
    assert get_service_name(9999) == "Unknown"


def test_zero_port():
    assert get_service_name(0) == "Unknown"


def test_negative_port():
    assert get_service_name(-1) == "Unknown"
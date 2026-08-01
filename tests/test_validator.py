"""
Unit Tests for NetSentry Validator Module
"""

from scanner.validator import (
    is_valid_ip,
    is_valid_hostname,
    is_valid_port,
    is_valid_port_range,
    is_valid_thread_count,
)


# -------------------------
# IP Validation
# -------------------------

def test_valid_ipv4():
    assert is_valid_ip("192.168.1.1")


def test_valid_ipv6():
    assert is_valid_ip("2001:db8::1")


def test_invalid_ip():
    assert not is_valid_ip("999.999.999.999")


# -------------------------
# Hostname Validation
# -------------------------

def test_valid_hostname():
    assert is_valid_hostname("google.com")


def test_localhost():
    assert is_valid_hostname("localhost")


def test_invalid_hostname():
    assert not is_valid_hostname("-google.com")


# -------------------------
# Port Validation
# -------------------------

def test_valid_port():
    assert is_valid_port(80)


def test_invalid_port_low():
    assert not is_valid_port(0)


def test_invalid_port_high():
    assert not is_valid_port(70000)


# -------------------------
# Port Range Validation
# -------------------------

def test_valid_port_range():
    assert is_valid_port_range(20, 80)


def test_invalid_port_range():
    assert not is_valid_port_range(100, 50)


# -------------------------
# Thread Count Validation
# -------------------------

def test_valid_thread_count():
    assert is_valid_thread_count(100)


def test_invalid_thread_count_low():
    assert not is_valid_thread_count(0)


def test_invalid_thread_count_high():
    assert not is_valid_thread_count(1000)
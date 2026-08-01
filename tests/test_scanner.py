"""
Unit Tests for NetSentry Scanner Module
"""

from unittest.mock import MagicMock, patch

import pytest

from scanner.scanner import PortScanner


# ---------------------------------------
# Resolve Target
# ---------------------------------------

@patch("scanner.scanner.socket.gethostbyname")
def test_resolve_target(mock_gethostbyname):
    mock_gethostbyname.return_value = "127.0.0.1"

    scanner = PortScanner("localhost")

    assert scanner.ip == "127.0.0.1"


@patch("scanner.scanner.socket.gethostbyname")
def test_invalid_target(mock_gethostbyname):
    import socket

    mock_gethostbyname.side_effect = socket.gaierror()

    with pytest.raises(ValueError):
        PortScanner("invalid-host")


# ---------------------------------------
# Scan Single Port
# ---------------------------------------

@patch("scanner.scanner.socket.socket")
@patch("scanner.scanner.socket.gethostbyname")
def test_scan_open_port(mock_gethostbyname, mock_socket):
    mock_gethostbyname.return_value = "127.0.0.1"

    sock = MagicMock()
    sock.connect_ex.return_value = 0

    mock_socket.return_value.__enter__.return_value = sock

    scanner = PortScanner("localhost")
    scanner.scan_port(80)

    assert 80 in scanner.get_results()


@patch("scanner.scanner.socket.socket")
@patch("scanner.scanner.socket.gethostbyname")
def test_scan_closed_port(mock_gethostbyname, mock_socket):
    mock_gethostbyname.return_value = "127.0.0.1"

    sock = MagicMock()
    sock.connect_ex.return_value = 1

    mock_socket.return_value.__enter__.return_value = sock

    scanner = PortScanner("localhost")
    scanner.scan_port(81)

    assert 81 not in scanner.get_results()


# ---------------------------------------
# Clear Results
# ---------------------------------------

@patch("scanner.scanner.socket.gethostbyname")
def test_clear_results(mock_gethostbyname):
    mock_gethostbyname.return_value = "127.0.0.1"

    scanner = PortScanner("localhost")

    scanner.open_ports = [22, 80, 443]

    scanner.clear_results()

    assert scanner.get_results() == []


# ---------------------------------------
# Scan Range
# ---------------------------------------

@patch.object(PortScanner, "scan_port")
@patch("scanner.scanner.socket.gethostbyname")
def test_scan_range(mock_gethostbyname, mock_scan_port):
    mock_gethostbyname.return_value = "127.0.0.1"

    scanner = PortScanner("localhost")

    scanner.scan_range(20, 25)

    assert mock_scan_port.call_count == 6
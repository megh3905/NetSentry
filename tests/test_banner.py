"""
Unit Tests for NetSentry Banner Grabbing Module
"""

from unittest.mock import MagicMock, patch

from scanner.banner import grab_banner


# ---------------------------------------
# HTTP Banner
# ---------------------------------------

@patch("scanner.banner.socket.create_connection")
def test_http_banner(mock_connection):
    mock_socket = MagicMock()
    mock_socket.recv.side_effect = [
        b"HTTP/1.1 200 OK\r\nServer: Apache\r\n\r\n",
        b"",
    ]

    mock_connection.return_value.__enter__.return_value = mock_socket

    assert grab_banner("127.0.0.1", 80) == "Apache"


# ---------------------------------------
# Generic Banner
# ---------------------------------------

@patch("scanner.banner.socket.create_connection")
def test_generic_banner(mock_connection):
    mock_socket = MagicMock()
    mock_socket.recv.return_value = b"SSH-2.0-OpenSSH_9.0"

    mock_connection.return_value.__enter__.return_value = mock_socket

    assert grab_banner("127.0.0.1", 22) == "SSH-2.0-OpenSSH_9.0"


# ---------------------------------------
# Open Port Without Banner
# ---------------------------------------

@patch("scanner.banner.socket.create_connection")
def test_open_without_banner(mock_connection):
    mock_socket = MagicMock()
    mock_socket.recv.return_value = b""

    mock_connection.return_value.__enter__.return_value = mock_socket

    assert grab_banner("127.0.0.1", 9999) == "Open"


# ---------------------------------------
# Connection Failure
# ---------------------------------------

@patch("scanner.banner.socket.create_connection")
def test_connection_failure(mock_connection):
    mock_connection.side_effect = Exception("Connection failed")

    assert grab_banner("127.0.0.1", 80) == "Unknown"
"""
NetSentry Banner Grabbing Module
--------------------------------
Advanced Banner Grabbing
"""

import socket
import ssl

from scanner.config import DEFAULT_TIMEOUT


def grab_banner(ip: str, port: int) -> str:
    """
    Grab service banner from an open port.
    """

    try:

        # ============================
        # HTTP
        # ============================

        if port == 80:

            with socket.create_connection((ip, port), timeout=DEFAULT_TIMEOUT) as sock:

                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {ip}\r\n"
                    "User-Agent: NetSentry/1.0\r\n"
                    "Connection: close\r\n\r\n"
                )

                sock.sendall(request.encode())

                response = b""

                while True:

                    data = sock.recv(4096)

                    if not data:
                        break

                    response += data

                response = response.decode(errors="ignore")

                for line in response.splitlines():

                    if line.lower().startswith("server:"):

                        return line.split(":", 1)[1].strip()

                return "HTTP"

        # ============================
        # HTTPS
        # ============================

        elif port == 443:

            context = ssl.create_default_context()

            with socket.create_connection((ip, port), timeout=DEFAULT_TIMEOUT) as sock:

                with context.wrap_socket(sock, server_hostname=ip) as ssock:

                    request = (
                        f"GET / HTTP/1.1\r\n"
                        f"Host: {ip}\r\n"
                        "User-Agent: NetSentry/1.0\r\n"
                        "Connection: close\r\n\r\n"
                    )

                    ssock.sendall(request.encode())

                    response = b""

                    while True:

                        data = ssock.recv(4096)

                        if not data:
                            break

                        response += data

                    response = response.decode(errors="ignore")

                    for line in response.splitlines():

                        if line.lower().startswith("server:"):

                            return line.split(":", 1)[1].strip()

                    return "HTTPS"

        # ============================
        # SSH / FTP / SMTP / Others
        # ============================

        else:

            with socket.create_connection((ip, port), timeout=DEFAULT_TIMEOUT) as sock:

                banner = sock.recv(1024).decode(errors="ignore").strip()

                if banner:

                    return banner

                return "Open"

    except Exception:

        return "Unknown"
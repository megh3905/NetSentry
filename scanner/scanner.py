"""
NetSentry Scanner Module
------------------------
Core TCP Port Scanner
"""

import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from scanner.config import DEFAULT_TIMEOUT
from scanner.logger import setup_logger


class PortScanner:
    """
    Core TCP Port Scanner
    """

    def __init__(self, target: str):

        self.target = target
        self.timeout = DEFAULT_TIMEOUT
        self.logger = setup_logger()

        self.open_ports = []

        # Resolve target only once
        self.ip = self.resolve_target()

    def resolve_target(self) -> str:
        """
        Resolve hostname into IP address.
        """

        try:
            return socket.gethostbyname(self.target)

        except socket.gaierror:
            raise ValueError("Invalid hostname or IP address.")

    def scan_port(self, port: int):
        """
        Scan a single TCP port.
        """

        try:

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

                sock.settimeout(self.timeout)

                result = sock.connect_ex((self.ip, port))

                if result == 0:

                    self.logger.info(f"Port {port} OPEN")

                    self.open_ports.append(port)

        except Exception as error:

            self.logger.error(error)

    def scan_range(self, start_port: int, end_port: int):
        """
        Scan a range of TCP ports using multithreading.
        """

        self.open_ports.clear()

        ports = list(range(start_port, end_port + 1))

        with ThreadPoolExecutor(max_workers=100) as executor:

            list(
                tqdm(
                    executor.map(self.scan_port, ports),
                    total=len(ports),
                    desc="Scanning",
                    unit="port"
                )
            )

        self.open_ports.sort()

        return self.open_ports

    def get_results(self):
        """
        Return all open ports.
        """

        return self.open_ports

    def clear_results(self):
        """
        Clear previous scan results.
        """

        self.open_ports.clear()
"""
NetSentry - Main Entry Point
Author: Megh Bhavsar
Version: 1.0.0
"""

import argparse
import time

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import box
from rich.live import Live

console = Console()

from scanner.config import APP_NAME, VERSION
from scanner.logger import setup_logger
from scanner.scanner import PortScanner
from scanner.service import get_service_name
from scanner.banner import grab_banner
from scanner.report import generate_reports
from scanner.history import save_scan_history
from scanner.colors import success, error, warning, info, title
from scanner.host import is_host_alive
from scanner.pdf_report import generate_pdf_report


def print_banner():
    """Display NetSentry ASCII banner."""

    ascii_banner = r"""
███╗   ██╗███████╗████████╗███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝
██╔██╗ ██║█████╗     ██║   █████╗  ██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝
██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝
██║ ╚████║███████╗   ██║   ███████╗██║ ╚████║   ██║   ██║  ██║   ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝
"""

    banner = Text()
    banner.append(ascii_banner, style="bold cyan")
    banner.append(
        "\nAdvanced Python Network Port Scanner",
        style="bold magenta"
    )
    banner.append(
        f"\nNetSentry v{VERSION}",
        style="bold yellow"
    )

    console.print(
        Panel(
            banner,
            border_style="bright_blue",
            box=box.DOUBLE,
            padding=(1, 2)
        )
    )


def parse_arguments():
    """
    Parse command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="NetSentry - Advanced Python Network Port Scanner"
    )

    parser.add_argument(
        "-t",
        "--target",
        help="Target IP address or Hostname"
    )

    parser.add_argument(
        "-s",
        "--start-port",
        type=int,
        help="Start Port"
    )

    parser.add_argument(
        "-e",
        "--end-port",
        type=int,
        help="End Port"
    )

    return parser.parse_args()


def main():
    """
    Main entry point of NetSentry.
    """

    args = parse_arguments()

    # Initialize logger
    logger = setup_logger()

    # Display banner
    print_banner()


    console.print(
                    "[bold green][+] NetSentry Started Successfully[/bold green]"
                )

    console.print(
                    "[bold green][+] Application Loaded Successfully[/bold green]"
                )

    console.print()

        # ======================================
        # Startup Animation
        # ======================================

    console.print(
                    "[bold cyan][*] Initializing Scanner Engine...[/bold cyan]"
                )

    for i in range(3):

        console.print(
                     f"[cyan]    Loading module {i + 1}/3...[/cyan]"
                 )
        time.sleep(0.25)

    console.print(
                    "[bold green][✓] Scanner Engine Ready[/bold green]"
                )

    console.print(
                    "[bold green][✓] Service Detection Ready[/bold green]"
                )

    console.print(
                    "[bold green][✓] Reporting Module Ready[/bold green]"
                )

    console.print()

# ======================================
# Target Input
# =======================================

    if args.target:
        target = args.target
    else:
        target = console.input(
                                "[bold cyan]Enter Target IP or Hostname: [/bold cyan]"
                            ).strip()
        
    # ======================================
    # Host Discovery
    # ======================================

    print(info("\nChecking target availability..."))

    if is_host_alive(target):
        print(success("✓ Host is Alive\n"))
    else:
        print(error("✗ Host is Unreachable"))
        return

    # ======================================
    # Initialize Scanner
    # ======================================

    try:
        scanner = PortScanner(target)

    except ValueError as exc:
        print(error(str(exc)))
        return

    # ======================================
    # Port Range
    # ======================================

    try:

        if args.start_port is not None and args.end_port is not None:
            start_port = args.start_port
            end_port = args.end_port

        else:
            start_port = int(input(info("Enter Start Port: ")))
            end_port = int(input(info("Enter End Port: ")))

    except ValueError:
        print(error("Invalid Port Number."))
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print(error("Invalid Port Range."))
        return

    # ======================================
    # Start Scan
    # ======================================

    print(info(f"\nScanning Ports {start_port} - {end_port}"))

    scanner.scan_range(start_port, end_port)

    # ======================================
    # Results
    # ======================================

    results = scanner.get_results()

    print(title("\n=========================================================================="))
    print(title("Open Ports"))
    print(title("=========================================================================="))

    report_data = []

    if results:

        print(info(f"{'PORT':<8}{'SERVICE':<20}{'BANNER'}"))
        print(info("-" * 74))

        for port in results:

            service = get_service_name(port)
            banner = grab_banner(scanner.ip, port)

            print(success(f"{port:<8}{service:<20}{banner}"))

            report_data.append([
                port,
                service,
                banner
            ])

        # Reports
        generate_reports(target, report_data)
        generate_pdf_report(target, report_data)

        # History
        save_scan_history(target, report_data)

        print(success("\n✓ Scan Completed Successfully."))

    else:
        print(warning("No Open Ports Found."))


if __name__ == "__main__":
    main()
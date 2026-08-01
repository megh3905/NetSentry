"""
NetSentry Service Detection Module
----------------------------------
Maps common TCP ports to service names.
"""

COMMON_SERVICES = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    111: "RPC",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL Server",
    1521: "Oracle Database",
    2049: "NFS",
    3306: "MySQL",
    3389: "Remote Desktop (RDP)",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Proxy",
    8443: "HTTPS Alternate",
    9200: "Elasticsearch",
    27017: "MongoDB"
}


def get_service_name(port: int) -> str:
    """
    Return the common service name for a TCP port.
    """

    return COMMON_SERVICES.get(port, "Unknown")
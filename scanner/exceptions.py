"""
NetSentry Custom Exceptions
---------------------------
Custom exception classes used across the application.
"""


class NetSentryError(Exception):
    """
    Base exception for all NetSentry errors.
    """
    pass


class InvalidIPAddressError(NetSentryError):
    """
    Raised when an invalid IP address is provided.
    """
    pass


class InvalidHostnameError(NetSentryError):
    """
    Raised when an invalid hostname is provided.
    """
    pass


class InvalidPortError(NetSentryError):
    """
    Raised when an invalid port number is provided.
    """
    pass


class InvalidPortRangeError(NetSentryError):
    """
    Raised when the port range is invalid.
    """
    pass


class InvalidThreadCountError(NetSentryError):
    """
    Raised when thread count is outside the allowed range.
    """
    pass


class HostUnreachableError(NetSentryError):
    """
    Raised when the target host cannot be reached.
    """
    pass


class ScanTimeoutError(NetSentryError):
    """
    Raised when a scan times out.
    """
    pass


class BannerGrabError(NetSentryError):
    """
    Raised when banner grabbing fails.
    """
    pass


class ReportGenerationError(NetSentryError):
    """
    Raised when report generation fails.
    """
    pass
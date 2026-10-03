# src/ipv4_validator/validator.py
"""Валидация IPv4-адресов."""

import re


_IPV4_RE = re.compile(
    r"^"
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    r"\Z"
)


def is_valid_ipv4(ipv4: str) -> bool:
    """Проверяет, является ли строка синтаксически корректным IPv4-адресом.

    Args:
        ipv4: строка для проверки.

    Returns:
        True, если адрес похож на корректный, иначе False.

    Examples:
        >>> is_valid_ipv4("192.168.1.1")
        True
        >>> is_valid_ipv4("999.999.999.999")
        False
    """
    if not isinstance(ipv4, str):
        return False
    if not ipv4:
        return False
    return _IPV4_RE.match(ipv4) is not None

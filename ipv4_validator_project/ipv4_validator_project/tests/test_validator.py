# tests/test_validator.py
import pytest

from ipv4_validator import is_valid_ipv4


def test_all_valid_fixture_ipv4(valid_ipv4):
    for ip in valid_ipv4:
        assert is_valid_ipv4(ip) is True, f"должен быть валидным: {ip!r}"


def test_all_invalid_fixture_ipv4(invalid_ipv4):
    for ip in invalid_ipv4:
        assert is_valid_ipv4(ip) is False, f"должен быть невалидным: {ip!r}"


def test_not_a_string():
    assert is_valid_ipv4(123) is False
    assert is_valid_ipv4(None) is False
    assert is_valid_ipv4(["192.168.1.1"]) is False

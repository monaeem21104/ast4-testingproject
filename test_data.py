"""
Test data utility for DemoBlaze automation tests.
Provides test data generation and management.
"""

import random
import string
from datetime import datetime


def generate_username(prefix="testuser"):
    """Generate a unique username for testing."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}_{timestamp}_{random_suffix}"


def generate_password(length=10):
    """Generate a random password for testing."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def generate_email(prefix="test"):
    """Generate a unique email for testing."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = ''.join(random.choices(string.digits, k=3))
    return f"{prefix}_{timestamp}_{random_suffix}@example.com"


def get_valid_order_data():
    """Get valid order form data."""
    return {
        "name": "John Doe",
        "country": "USA",
        "city": "New York",
        "credit_card": "1234567890123456",
        "month": "12",
        "year": "2025"
    }


def get_invalid_order_data():
    """Get invalid order form data for negative testing."""
    return {
        "name": "",  # Empty name
        "country": "USA",
        "city": "New York",
        "credit_card": "abc123",  # Invalid credit card
        "month": "13",  # Invalid month
        "year": "2020"  # Past year
    }


def get_test_products():
    """Get sample test products."""
    return {
        "phones": ["Samsung galaxy s6", "Nexus 6", "Iphone 6 32gb"],
        "laptops": ["MacBook air", "Sony vaio i5", "Dell i7 8gb"],
        "monitors": ["Apple monitor 24", "ASUS Full HD"]
    }


def get_xss_payloads():
    """Get XSS test payloads for security testing."""
    return [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>",
        "javascript:alert('XSS')"
    ]


def get_sql_injection_payloads():
    """Get SQL injection test payloads for security testing."""
    return [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "admin'--"
    ]


"""
Configuration module for DemoBlaze automation tests.
Contains base URL, browser settings, and other configuration.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Base URL
BASE_URL = os.getenv("BASE_URL", "https://www.demoblaze.com/")

# Browser configuration
BROWSER = os.getenv("BROWSER", "chrome").lower()  # chrome, firefox, edge, safari
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))  # seconds
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))  # seconds

# Screenshot configuration
SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR", "automation/screenshots")
SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

# Test data configuration
TEST_DATA_DIR = os.getenv("TEST_DATA_DIR", "automation/test_data")

# Reporting configuration
REPORT_DIR = os.getenv("REPORT_DIR", "automation/reports")
HTML_REPORT = os.path.join(REPORT_DIR, "report.html")
JUNIT_XML = os.path.join(REPORT_DIR, "junit.xml")

# Retry configuration
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "2"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "1"))  # seconds

# Browser window configuration
WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", "1920"))
WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", "1080"))


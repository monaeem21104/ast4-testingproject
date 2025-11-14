"""
Logger utility for DemoBlaze automation tests.
Provides centralized logging functionality.
"""

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "automation/logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create logger
logger = logging.getLogger("demoblaze_automation")
logger.setLevel(logging.DEBUG)

# Create file handler
log_file = os.path.join(LOG_DIR, f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Add formatter to handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def get_logger():
    """Get the logger instance."""
    return logger


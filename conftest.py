"""
Pytest configuration and fixtures for DemoBlaze automation tests.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from automation.utils.config import (
    BASE_URL, BROWSER, HEADLESS, WINDOW_WIDTH, WINDOW_HEIGHT,
    SCREENSHOT_ON_FAILURE, SCREENSHOT_DIR
)
from automation.utils.logger import get_logger
import os

logger = get_logger()


@pytest.fixture(scope="function")
def driver():
    """Create and configure WebDriver instance."""
    driver = None
    
    try:
        if BROWSER == "chrome":
            options = Options()
            if HEADLESS:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
        elif BROWSER == "firefox":
            options = FirefoxOptions()
            if HEADLESS:
                options.add_argument("--headless")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
            
        elif BROWSER == "edge":
            options = EdgeOptions()
            if HEADLESS:
                options.add_argument("--headless")
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
            driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
            
        else:
            raise ValueError(f"Unsupported browser: {BROWSER}")
        
        logger.info(f"WebDriver initialized: {BROWSER} (headless={HEADLESS})")
        yield driver
        
    except Exception as e:
        logger.error(f"Error initializing WebDriver: {e}")
        raise
    finally:
        if driver:
            driver.quit()
            logger.info("WebDriver closed")


@pytest.fixture(scope="function")
def home_page(driver):
    """Create HomePage instance."""
    from automation.pages.home_page import HomePage
    page = HomePage(driver)
    page.open(BASE_URL)
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on test failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed and SCREENSHOT_ON_FAILURE:
        try:
            # Get driver from fixture
            driver = item.funcargs.get("driver")
            if driver:
                # Create screenshot directory if it doesn't exist
                os.makedirs(SCREENSHOT_DIR, exist_ok=True)
                
                # Take screenshot
                screenshot_path = os.path.join(
                    SCREENSHOT_DIR,
                    f"{item.name}_{rep.when}_failure.png"
                )
                driver.save_screenshot(screenshot_path)
                logger.info(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            logger.error(f"Error taking screenshot: {e}")


def pytest_configure(config):
    """Pytest configuration."""
    # Create necessary directories
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    logger.info("Pytest configured")


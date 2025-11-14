"""
Base page class for DemoBlaze automation tests.
Provides common functionality for all page objects.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from automation.utils.config import EXPLICIT_WAIT
from automation.utils.logger import get_logger

logger = get_logger()


class BasePage:
    """Base page class with common methods for all page objects."""

    def __init__(self, driver):
        """Initialize base page with driver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
        self.logger = logger

    def open(self, url):
        """Open a URL."""
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self, locator):
        """Find an element with explicit wait."""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise

    def find_elements(self, locator):
        """Find multiple elements with explicit wait."""
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            self.logger.debug(f"Found {len(elements)} elements: {locator}")
            return elements
        except TimeoutException:
            self.logger.warning(f"Elements not found: {locator}")
            return []

    def click_element(self, locator):
        """Click an element with explicit wait."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            raise

    def send_keys(self, locator, text):
        """Send keys to an element with explicit wait."""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Sent keys to element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not found for sending keys: {locator}")
            raise

    def get_text(self, locator):
        """Get text from an element."""
        try:
            element = self.find_element(locator)
            text = element.text
            self.logger.debug(f"Got text from element: {locator} - {text}")
            return text
        except TimeoutException:
            self.logger.error(f"Could not get text from element: {locator}")
            raise

    def is_element_present(self, locator):
        """Check if an element is present."""
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator):
        """Check if an element is visible."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_alert(self, timeout=None):
        """Wait for an alert to appear."""
        if timeout is None:
            timeout = EXPLICIT_WAIT
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            self.logger.info("Alert is present")
            return alert
        except TimeoutException:
            self.logger.warning("Alert not present within timeout")
            return None

    def accept_alert(self):
        """Accept an alert."""
        try:
            alert = self.wait_for_alert()
            if alert:
                alert.accept()
                self.logger.info("Alert accepted")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error accepting alert: {e}")
            return False

    def get_page_title(self):
        """Get the page title."""
        return self.driver.title

    def get_current_url(self):
        """Get the current URL."""
        return self.driver.current_url

    def take_screenshot(self, filename):
        """Take a screenshot."""
        try:
            self.driver.save_screenshot(filename)
            self.logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")


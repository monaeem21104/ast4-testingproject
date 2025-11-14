"""
Login page object for DemoBlaze automation tests.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object class."""

    # Locators
    LOGIN_MODAL = (By.CSS_SELECTOR, "#logInModal")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#loginusername")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log in')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'Close')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        """Initialize login page."""
        super().__init__(driver)

    def is_login_modal_displayed(self):
        """Check if login modal is displayed."""
        return self.is_element_visible(self.LOGIN_MODAL)

    def fill_username(self, username):
        """Fill username field."""
        self.send_keys(self.USERNAME_FIELD, username)

    def fill_password(self, password):
        """Fill password field."""
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login(self):
        """Click Log in button."""
        self.click_element(self.LOGIN_BUTTON)

    def click_close(self):
        """Click Close button."""
        self.click_element(self.CLOSE_BUTTON)

    def login(self, username, password):
        """Complete login process."""
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
        # Wait for alert or navigation update
        alert_present = self.wait_for_alert(timeout=5)
        return alert_present

    def get_error_message(self):
        """Get error message if present."""
        try:
            error = self.find_element(self.ERROR_MESSAGE)
            return error.text
        except Exception:
            return ""

    def verify_validation_error(self):
        """Verify that validation error is displayed."""
        return self.is_element_present(self.ERROR_MESSAGE)


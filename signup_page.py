"""
Signup page object for DemoBlaze automation tests.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from automation.pages.base_page import BasePage


class SignupPage(BasePage):
    """Signup page object class."""

    # Locators
    SIGNUP_MODAL = (By.CSS_SELECTOR, "#signInModal")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#sign-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign up')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'Close')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        """Initialize signup page."""
        super().__init__(driver)

    def is_signup_modal_displayed(self):
        """Check if signup modal is displayed."""
        return self.is_element_visible(self.SIGNUP_MODAL)

    def fill_username(self, username):
        """Fill username field."""
        self.send_keys(self.USERNAME_FIELD, username)

    def fill_password(self, password):
        """Fill password field."""
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_signup(self):
        """Click Sign up button."""
        self.click_element(self.SIGNUP_BUTTON)

    def click_close(self):
        """Click Close button."""
        self.click_element(self.CLOSE_BUTTON)

    def signup(self, username, password):
        """Complete signup process."""
        self.fill_username(username)
        self.fill_password(password)
        self.click_signup()
        # Wait for alert or error message
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


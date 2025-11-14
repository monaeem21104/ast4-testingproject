"""
Checkout/Order page object for DemoBlaze automation tests.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from automation.pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Checkout page object class."""

    # Locators
    ORDER_MODAL = (By.CSS_SELECTOR, "#orderModal")
    NAME_FIELD = (By.CSS_SELECTOR, "#name")
    COUNTRY_FIELD = (By.CSS_SELECTOR, "#country")
    CITY_FIELD = (By.CSS_SELECTOR, "#city")
    CREDIT_CARD_FIELD = (By.CSS_SELECTOR, "#card")
    MONTH_FIELD = (By.CSS_SELECTOR, "#month")
    YEAR_FIELD = (By.CSS_SELECTOR, "#year")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(), 'Purchase')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'Close')]")
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, ".sweet-alert")

    def __init__(self, driver):
        """Initialize checkout page."""
        super().__init__(driver)

    def is_order_modal_displayed(self):
        """Check if order modal is displayed."""
        return self.is_element_visible(self.ORDER_MODAL)

    def fill_name(self, name):
        """Fill name field."""
        self.send_keys(self.NAME_FIELD, name)

    def fill_country(self, country):
        """Fill country field."""
        self.send_keys(self.COUNTRY_FIELD, country)

    def fill_city(self, city):
        """Fill city field."""
        self.send_keys(self.CITY_FIELD, city)

    def fill_credit_card(self, credit_card):
        """Fill credit card field."""
        self.send_keys(self.CREDIT_CARD_FIELD, credit_card)

    def fill_month(self, month):
        """Fill month field."""
        self.send_keys(self.MONTH_FIELD, month)

    def fill_year(self, year):
        """Fill year field."""
        self.send_keys(self.YEAR_FIELD, year)

    def fill_order_form(self, order_data):
        """Fill complete order form with order data."""
        self.fill_name(order_data.get("name", ""))
        self.fill_country(order_data.get("country", ""))
        self.fill_city(order_data.get("city", ""))
        self.fill_credit_card(order_data.get("credit_card", ""))
        self.fill_month(order_data.get("month", ""))
        self.fill_year(order_data.get("year", ""))

    def click_purchase(self):
        """Click Purchase button."""
        self.click_element(self.PURCHASE_BUTTON)

    def click_close(self):
        """Click Close button."""
        self.click_element(self.CLOSE_BUTTON)

    def place_order(self, order_data):
        """Place order with provided order data."""
        self.fill_order_form(order_data)
        self.click_purchase()
        # Wait for confirmation
        confirmation_present = self.wait_for_order_confirmation()
        return confirmation_present

    def wait_for_order_confirmation(self, timeout=10):
        """Wait for order confirmation to appear."""
        try:
            wait = self.wait
            confirmation = wait.until(EC.presence_of_element_located(self.ORDER_CONFIRMATION))
            return True
        except Exception:
            return False

    def get_order_confirmation_text(self):
        """Get order confirmation text."""
        try:
            return self.get_text(self.ORDER_CONFIRMATION)
        except Exception:
            return ""

    def verify_all_fields_present(self):
        """Verify that all order form fields are present."""
        fields = [
            self.NAME_FIELD,
            self.COUNTRY_FIELD,
            self.CITY_FIELD,
            self.CREDIT_CARD_FIELD,
            self.MONTH_FIELD,
            self.YEAR_FIELD
        ]
        all_present = True
        for field in fields:
            if not self.is_element_present(field):
                all_present = False
                self.logger.warning(f"Field not found: {field}")
        return all_present


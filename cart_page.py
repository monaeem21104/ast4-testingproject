"""
Cart page object for DemoBlaze automation tests.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage
import re


class CartPage(BasePage):
    """Cart page object class."""

    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, "tbody tr")
    PRODUCT_NAME = (By.CSS_SELECTOR, "td:nth-child(2)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "td:nth-child(3)")
    DELETE_BUTTON = (By.XPATH, "//a[contains(text(), 'Delete')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")
    TOTAL_PRICE = (By.CSS_SELECTOR, "#totalp")
    EMPTY_CART_MESSAGE = (By.XPATH, "//tbody//td[contains(text(), 'No items')]")

    def __init__(self, driver):
        """Initialize cart page."""
        super().__init__(driver)

    def get_cart_items(self):
        """Get list of cart items."""
        items = self.find_elements(self.CART_ITEMS)
        return items

    def get_cart_item_count(self):
        """Get the number of items in cart."""
        items = self.get_cart_items()
        return len(items)

    def is_cart_empty(self):
        """Check if cart is empty."""
        items = self.get_cart_items()
        return len(items) == 0

    def get_product_names_in_cart(self):
        """Get list of product names in cart."""
        product_names = []
        items = self.get_cart_items()
        for item in items:
            try:
                name_element = item.find_element(*self.PRODUCT_NAME)
                product_names.append(name_element.text)
            except Exception:
                continue
        return product_names

    def get_product_prices_in_cart(self):
        """Get list of product prices in cart."""
        product_prices = []
        items = self.get_cart_items()
        for item in items:
            try:
                price_element = item.find_element(*self.PRODUCT_PRICE)
                price_text = price_element.text
                # Extract numeric price
                price = re.findall(r'\d+', price_text)
                if price:
                    product_prices.append(int(price[0]))
            except Exception:
                continue
        return product_prices

    def get_total_price(self):
        """Get the total price from cart."""
        try:
            total_text = self.get_text(self.TOTAL_PRICE)
            # Extract numeric price
            total = re.findall(r'\d+', total_text)
            if total:
                return int(total[0])
            return 0
        except Exception:
            return 0

    def calculate_expected_total(self):
        """Calculate expected total from individual prices."""
        prices = self.get_product_prices_in_cart()
        return sum(prices)

    def verify_total_calculation(self):
        """Verify that cart total matches sum of individual prices."""
        expected_total = self.calculate_expected_total()
        actual_total = self.get_total_price()
        return expected_total == actual_total

    def delete_first_item(self):
        """Delete the first item from cart."""
        try:
            delete_buttons = self.find_elements(self.DELETE_BUTTON)
            if delete_buttons:
                delete_buttons[0].click()
                self.logger.info("Deleted first item from cart")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting item: {e}")
            return False

    def click_place_order(self):
        """Click Place Order button."""
        self.click_element(self.PLACE_ORDER_BUTTON)

    def verify_place_order_button_present(self):
        """Verify that Place Order button is present."""
        return self.is_element_present(self.PLACE_ORDER_BUTTON)

    def verify_empty_cart_message(self):
        """Verify that empty cart message is displayed."""
        return self.is_element_present(self.EMPTY_CART_MESSAGE)


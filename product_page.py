"""
Product page object for DemoBlaze automation tests.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage


class ProductPage(BasePage):
    """Product page object class."""

    # Locators
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price-container")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#more-information p")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".item-img")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[contains(text(), 'Add to cart')]")
    
    # Product list locators
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".card")
    PRODUCT_LINK = (By.CSS_SELECTOR, ".hrefch")

    def __init__(self, driver):
        """Initialize product page."""
        super().__init__(driver)

    def get_product_name(self):
        """Get product name."""
        return self.get_text(self.PRODUCT_NAME)

    def get_product_price(self):
        """Get product price."""
        price_text = self.get_text(self.PRODUCT_PRICE)
        # Extract price from text (e.g., "$360 *includes tax")
        return price_text

    def verify_product_details(self):
        """Verify that product details are displayed."""
        details_present = (
            self.is_element_visible(self.PRODUCT_NAME) and
            self.is_element_visible(self.PRODUCT_PRICE) and
            self.is_element_visible(self.PRODUCT_IMAGE) and
            self.is_element_visible(self.ADD_TO_CART_BUTTON)
        )
        return details_present

    def click_add_to_cart(self):
        """Click Add to cart button."""
        self.click_element(self.ADD_TO_CART_BUTTON)

    def add_product_to_cart(self):
        """Add product to cart and handle alert."""
        self.click_add_to_cart()
        # Wait for and accept alert
        alert_accepted = self.accept_alert()
        return alert_accepted

    def click_product_by_name(self, product_name):
        """Click on a product by name from product list."""
        try:
            # Find product link by text
            product_link = (By.XPATH, f"//a[contains(text(), '{product_name}')]")
            self.click_element(product_link)
            return True
        except Exception as e:
            self.logger.error(f"Error clicking product {product_name}: {e}")
            return False

    def get_product_list(self):
        """Get list of products on the page."""
        products = self.find_elements(self.PRODUCT_ITEMS)
        return products

    def verify_product_list_displayed(self):
        """Verify that product list is displayed."""
        products = self.get_product_list()
        return len(products) > 0


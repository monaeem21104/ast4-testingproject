"""
Home page object for DemoBlaze automation tests.
"""

from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage


class HomePage(BasePage):
    """Home page object class."""

    # Locators
    HEADER_TITLE = (By.XPATH, "//a[@class='navbar-brand' and contains(text(), 'PRODUCT STORE')]")
    NAV_HOME = (By.XPATH, "//a[contains(text(), 'Home')]")
    NAV_CONTACT = (By.XPATH, "//a[contains(text(), 'Contact')]")
    NAV_ABOUT_US = (By.XPATH, "//a[contains(text(), 'About us')]")
    NAV_CART = (By.XPATH, "//a[contains(text(), 'Cart')]")
    NAV_LOGIN = (By.XPATH, "//a[contains(text(), 'Log in')]")
    NAV_LOGOUT = (By.XPATH, "//a[contains(text(), 'Log out')]")
    NAV_SIGNUP = (By.XPATH, "//a[contains(text(), 'Sign up')]")
    
    CATEGORY_PHONES = (By.XPATH, "//a[contains(text(), 'Phones')]")
    CATEGORY_LAPTOPS = (By.XPATH, "//a[contains(text(), 'Laptops')]")
    CATEGORY_MONITORS = (By.XPATH, "//a[contains(text(), 'Monitors')]")
    
    CAROUSEL_NEXT = (By.CSS_SELECTOR, ".carousel-control-next")
    CAROUSEL_PREV = (By.CSS_SELECTOR, ".carousel-control-prev")
    
    FOOTER_COPYRIGHT = (By.XPATH, "//footer//p[contains(text(), 'Copyright')]")

    def __init__(self, driver):
        """Initialize home page."""
        super().__init__(driver)

    def verify_header_displayed(self):
        """Verify that header is displayed."""
        return self.is_element_visible(self.HEADER_TITLE)

    def verify_navigation_menu(self):
        """Verify that navigation menu is present."""
        nav_items = [
            self.NAV_HOME,
            self.NAV_CONTACT,
            self.NAV_ABOUT_US,
            self.NAV_CART,
            self.NAV_LOGIN,
            self.NAV_SIGNUP
        ]
        all_present = True
        for nav_item in nav_items:
            if not self.is_element_present(nav_item):
                all_present = False
                self.logger.warning(f"Navigation item not found: {nav_item}")
        return all_present

    def verify_categories_displayed(self):
        """Verify that product categories are displayed."""
        categories = [
            self.CATEGORY_PHONES,
            self.CATEGORY_LAPTOPS,
            self.CATEGORY_MONITORS
        ]
        all_present = True
        for category in categories:
            if not self.is_element_present(category):
                all_present = False
                self.logger.warning(f"Category not found: {category}")
        return all_present

    def click_category_phones(self):
        """Click on Phones category."""
        self.click_element(self.CATEGORY_PHONES)

    def click_category_laptops(self):
        """Click on Laptops category."""
        self.click_element(self.CATEGORY_LAPTOPS)

    def click_category_monitors(self):
        """Click on Monitors category."""
        self.click_element(self.CATEGORY_MONITORS)

    def click_cart(self):
        """Click on Cart link."""
        self.click_element(self.NAV_CART)

    def click_login(self):
        """Click on Log in link."""
        self.click_element(self.NAV_LOGIN)

    def click_signup(self):
        """Click on Sign up link."""
        self.click_element(self.NAV_SIGNUP)

    def click_logout(self):
        """Click on Log out link."""
        self.click_element(self.NAV_LOGOUT)

    def is_logged_in(self):
        """Check if user is logged in (Log out link is visible)."""
        return self.is_element_present(self.NAV_LOGOUT)

    def verify_carousel_functionality(self):
        """Verify that carousel Previous/Next buttons work."""
        try:
            # Click Next
            if self.is_element_present(self.CAROUSEL_NEXT):
                self.click_element(self.CAROUSEL_NEXT)
            # Click Previous
            if self.is_element_present(self.CAROUSEL_PREV):
                self.click_element(self.CAROUSEL_PREV)
            return True
        except Exception as e:
            self.logger.error(f"Carousel functionality error: {e}")
            return False

    def verify_footer_copyright(self):
        """Verify that footer copyright is displayed."""
        return self.is_element_visible(self.FOOTER_COPYRIGHT)


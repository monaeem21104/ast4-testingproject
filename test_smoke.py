"""
Smoke tests for DemoBlaze application.
These tests validate critical functionality quickly.
"""

import pytest
from automation.pages.home_page import HomePage
from automation.pages.product_page import ProductPage
from automation.utils.config import BASE_URL
from automation.utils.logger import get_logger

logger = get_logger()


class TestSmoke:
    """Smoke test suite."""

    def test_homepage_loads(self, driver):
        """Test that homepage loads successfully."""
        logger.info("Test: Homepage loads")
        home_page = HomePage(driver)
        home_page.open(BASE_URL)
        
        # Verify header is displayed
        assert home_page.verify_header_displayed(), "Header not displayed"
        
        # Verify navigation menu
        assert home_page.verify_navigation_menu(), "Navigation menu not complete"
        
        # Verify categories
        assert home_page.verify_categories_displayed(), "Categories not displayed"
        
        logger.info("Homepage loads successfully")

    def test_category_navigation(self, driver):
        """Test that category navigation works."""
        logger.info("Test: Category navigation")
        home_page = HomePage(driver)
        home_page.open(BASE_URL)
        
        # Test Phones category
        home_page.click_category_phones()
        product_page = ProductPage(driver)
        assert product_page.verify_product_list_displayed(), "Phones category not working"
        
        # Test Laptops category
        home_page.open(BASE_URL)
        home_page.click_category_laptops()
        assert product_page.verify_product_list_displayed(), "Laptops category not working"
        
        logger.info("Category navigation works correctly")

    def test_product_listing(self, driver):
        """Test that product listing is displayed."""
        logger.info("Test: Product listing")
        home_page = HomePage(driver)
        home_page.open(BASE_URL)
        home_page.click_category_phones()
        
        product_page = ProductPage(driver)
        assert product_page.verify_product_list_displayed(), "Product list not displayed"
        
        products = product_page.get_product_list()
        assert len(products) > 0, "No products found"
        
        logger.info(f"Product listing displayed: {len(products)} products")

    def test_product_detail_view(self, driver):
        """Test that product detail page opens."""
        logger.info("Test: Product detail view")
        home_page = HomePage(driver)
        home_page.open(BASE_URL)
        home_page.click_category_phones()
        
        product_page = ProductPage(driver)
        # Click on first product
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        if product_links:
            product_links[0].click()
            
            # Verify product details
            assert product_page.verify_product_details(), "Product details not displayed"
            
            product_name = product_page.get_product_name()
            assert product_name, f"Product name not found: {product_name}"
            
            logger.info(f"Product detail view works: {product_name}")
        else:
            pytest.fail("No products found to test")

    def test_add_to_cart_smoke(self, driver):
        """Test that add to cart functionality works."""
        logger.info("Test: Add to cart smoke")
        home_page = HomePage(driver)
        home_page.open(BASE_URL)
        home_page.click_category_phones()
        
        product_page = ProductPage(driver)
        # Click on first product
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        if product_links:
            product_links[0].click()
            
            # Add to cart
            alert_accepted = product_page.add_product_to_cart()
            assert alert_accepted, "Add to cart failed - alert not accepted"
            
            logger.info("Add to cart works correctly")
        else:
            pytest.fail("No products found to test")


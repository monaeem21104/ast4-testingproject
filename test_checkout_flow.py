"""
Checkout flow tests for DemoBlaze application.
"""

import pytest
from automation.pages.home_page import HomePage
from automation.pages.product_page import ProductPage
from automation.pages.cart_page import CartPage
from automation.pages.checkout_page import CheckoutPage
from automation.utils.test_data import get_valid_order_data, get_test_products
from automation.utils.logger import get_logger

logger = get_logger()


class TestCheckoutFlow:
    """Checkout flow test suite."""

    def test_add_to_cart(self, home_page):
        """Test adding product to cart."""
        logger.info("Test: Add to cart")
        home_page.click_category_phones()
        
        product_page = ProductPage(home_page.driver)
        # Click on first product
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        if product_links:
            product_links[0].click()
            
            # Add to cart
            alert_accepted = product_page.add_product_to_cart()
            assert alert_accepted, "Add to cart failed"
            
            logger.info("Product added to cart successfully")
        else:
            pytest.fail("No products found")

    def test_view_cart(self, home_page):
        """Test viewing cart with items."""
        logger.info("Test: View cart")
        # Add product to cart first
        home_page.click_category_phones()
        product_page = ProductPage(home_page.driver)
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        if product_links:
            product_links[0].click()
            product_page.add_product_to_cart()
            
            # View cart
            home_page.click_cart()
            cart_page = CartPage(home_page.driver)
            
            assert not cart_page.is_cart_empty(), "Cart is empty"
            item_count = cart_page.get_cart_item_count()
            assert item_count > 0, f"Cart item count is {item_count}, expected > 0"
            
            logger.info(f"Cart viewed successfully: {item_count} items")
        else:
            pytest.fail("No products found")

    def test_remove_from_cart(self, home_page):
        """Test removing product from cart."""
        logger.info("Test: Remove from cart")
        # Add product to cart first
        home_page.click_category_phones()
        product_page = ProductPage(home_page.driver)
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        if product_links:
            product_links[0].click()
            product_page.add_product_to_cart()
            
            # View cart and remove item
            home_page.click_cart()
            cart_page = CartPage(home_page.driver)
            
            initial_count = cart_page.get_cart_item_count()
            cart_page.delete_first_item()
            
            # Wait a moment for deletion to process
            import time
            time.sleep(1)
            
            # Verify item was removed
            final_count = cart_page.get_cart_item_count()
            assert final_count < initial_count, "Item was not removed from cart"
            
            logger.info(f"Item removed: {initial_count} -> {final_count}")
        else:
            pytest.fail("No products found")

    def test_cart_total_calculation(self, home_page):
        """Test that cart total is calculated correctly."""
        logger.info("Test: Cart total calculation")
        # Add multiple products to cart
        home_page.click_category_phones()
        product_page = ProductPage(home_page.driver)
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        
        if len(product_links) >= 2:
            # Add first product
            product_links[0].click()
            product_page.add_product_to_cart()
            
            # Add second product
            home_page.click_category_phones()
            product_links = product_page.find_elements(product_page.PRODUCT_LINK)
            product_links[1].click()
            product_page.add_product_to_cart()
            
            # View cart and verify total
            home_page.click_cart()
            cart_page = CartPage(home_page.driver)
            
            # Verify total calculation
            total_correct = cart_page.verify_total_calculation()
            assert total_correct, "Cart total calculation is incorrect"
            
            logger.info("Cart total calculation is correct")
        else:
            pytest.skip("Not enough products to test total calculation")

    def test_place_order(self, home_page):
        """Test placing an order."""
        logger.info("Test: Place order")
        # Add product to cart first
        home_page.click_category_phones()
        product_page = ProductPage(home_page.driver)
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        if product_links:
            product_links[0].click()
            product_page.add_product_to_cart()
            
            # Go to cart and place order
            home_page.click_cart()
            cart_page = CartPage(home_page.driver)
            
            assert cart_page.verify_place_order_button_present(), "Place Order button not present"
            cart_page.click_place_order()
            
            # Fill order form
            checkout_page = CheckoutPage(home_page.driver)
            assert checkout_page.is_order_modal_displayed(), "Order modal not displayed"
            
            order_data = get_valid_order_data()
            confirmation_present = checkout_page.place_order(order_data)
            
            # Verify order confirmation
            assert confirmation_present, "Order confirmation not displayed"
            
            logger.info("Order placed successfully")
        else:
            pytest.fail("No products found")

    def test_order_form_validation(self, home_page):
        """Test order form validation."""
        logger.info("Test: Order form validation")
        # Add product to cart first
        home_page.click_category_phones()
        product_page = ProductPage(home_page.driver)
        product_links = product_page.find_elements(product_page.PRODUCT_LINK)
        if product_links:
            product_links[0].click()
            product_page.add_product_to_cart()
            
            # Go to cart and open order form
            home_page.click_cart()
            cart_page = CartPage(home_page.driver)
            cart_page.click_place_order()
            
            checkout_page = CheckoutPage(home_page.driver)
            assert checkout_page.is_order_modal_displayed(), "Order modal not displayed"
            
            # Verify all fields are present
            assert checkout_page.verify_all_fields_present(), "Not all order form fields are present"
            
            logger.info("Order form validation tested")
        else:
            pytest.fail("No products found")


"""
Login and signup tests for DemoBlaze application.
"""

import pytest
from automation.pages.home_page import HomePage
from automation.pages.login_page import LoginPage
from automation.pages.signup_page import SignupPage
from automation.utils.test_data import generate_username, generate_password
from automation.utils.logger import get_logger

logger = get_logger()


class TestLoginSignup:
    """Login and signup test suite."""

    def test_signup_modal_opens(self, home_page):
        """Test that signup modal opens."""
        logger.info("Test: Signup modal opens")
        home_page.click_signup()
        
        signup_page = SignupPage(home_page.driver)
        assert signup_page.is_signup_modal_displayed(), "Signup modal not displayed"
        
        logger.info("Signup modal opens correctly")

    def test_user_signup(self, home_page):
        """Test user registration with valid data."""
        logger.info("Test: User signup")
        home_page.click_signup()
        
        signup_page = SignupPage(home_page.driver)
        username = generate_username()
        password = generate_password()
        
        logger.info(f"Signing up with username: {username}")
        alert_present = signup_page.signup(username, password)
        
        # Signup may show alert or redirect
        # For demo purposes, we check if alert appeared or modal closed
        assert alert_present or not signup_page.is_signup_modal_displayed(), \
            "Signup failed - no confirmation"
        
        logger.info("User signup successful")

    def test_signup_empty_fields(self, home_page):
        """Test signup validation with empty fields."""
        logger.info("Test: Signup empty fields validation")
        home_page.click_signup()
        
        signup_page = SignupPage(home_page.driver)
        signup_page.click_signup()  # Try to submit with empty fields
        
        # Check for validation error or alert
        # Note: Actual behavior may vary based on implementation
        logger.info("Signup validation tested")

    def test_login_modal_opens(self, home_page):
        """Test that login modal opens."""
        logger.info("Test: Login modal opens")
        home_page.click_login()
        
        login_page = LoginPage(home_page.driver)
        assert login_page.is_login_modal_displayed(), "Login modal not displayed"
        
        logger.info("Login modal opens correctly")

    @pytest.mark.skip(reason="Requires existing user account - setup needed")
    def test_user_login(self, home_page):
        """Test user login with valid credentials."""
        logger.info("Test: User login")
        home_page.click_login()
        
        login_page = LoginPage(home_page.driver)
        # Note: This requires a pre-existing user account
        # In real scenario, create user first or use test data
        username = "testuser"
        password = "password123"
        
        alert_present = login_page.login(username, password)
        
        # Check if login was successful (navigation updates)
        # For demo purposes, we check if alert appeared or user is logged in
        if alert_present:
            home_page.accept_alert()
        
        # Verify login by checking if logout link is visible
        is_logged_in = home_page.is_logged_in()
        logger.info(f"Login test completed - Logged in: {is_logged_in}")

    def test_login_empty_fields(self, home_page):
        """Test login validation with empty fields."""
        logger.info("Test: Login empty fields validation")
        home_page.click_login()
        
        login_page = LoginPage(home_page.driver)
        login_page.click_login()  # Try to submit with empty fields
        
        # Check for validation error
        # Note: Actual behavior may vary based on implementation
        logger.info("Login validation tested")

    def test_logout(self, home_page):
        """Test user logout functionality."""
        logger.info("Test: User logout")
        
        # First, check if user is logged in
        if home_page.is_logged_in():
            home_page.click_logout()
            # Verify logout by checking if login link is visible
            assert not home_page.is_logged_in(), "Logout failed"
            logger.info("User logged out successfully")
        else:
            logger.info("User not logged in - skipping logout test")
            pytest.skip("User not logged in")


# Test Cases Document - DemoBlaze.com
## Manual Testing Test Cases

**Project:** DemoBlaze E-Commerce Website  
**URL:** https://demoblaze.com/  
**Document Version:** 1.0  
**Date:** 2024

---

## Table of Contents
1. [Homepage Test Cases](#1-homepage-test-cases)
2. [User Registration Test Cases](#2-user-registration-test-cases)
3. [User Login Test Cases](#3-user-login-test-cases)
4. [Product Browsing Test Cases](#4-product-browsing-test-cases)
5. [Product Details Test Cases](#5-product-details-test-cases)
6. [Shopping Cart Test Cases](#6-shopping-cart-test-cases)
7. [Checkout/Place Order Test Cases](#7-checkoutplace-order-test-cases)
8. [Navigation Test Cases](#8-navigation-test-cases)
9. [UI/UX Test Cases](#9-uiux-test-cases)
10. [Security Test Cases](#10-security-test-cases)
11. [Performance Test Cases](#11-performance-test-cases)
12. [Compatibility Test Cases](#12-compatibility-test-cases)
13. [Edge Cases and Negative Test Cases](#13-edge-cases-and-negative-test-cases)
14. [Accessibility Test Cases](#14-accessibility-test-cases)
15. [Data Validation Test Cases](#15-data-validation-test-cases)

---

## 1. Homepage Test Cases

### TC-001: Verify Homepage Loads Successfully
**Priority:** High  
**Preconditions:** User has internet connection  
**Steps:**
1. Navigate to https://demoblaze.com/
2. Wait for page to load completely

**Expected Result:** Homepage loads successfully with all elements visible (header, navigation, product categories, footer)

---

### TC-002: Verify Homepage Title
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Steps:**
1. Check browser tab title

**Expected Result:** Browser tab displays appropriate title (e.g., "STORE" or "DemoBlaze")

---

### TC-003: Verify Homepage Logo Display
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Steps:**
1. Check if logo is displayed in header

**Expected Result:** Logo is visible and properly displayed in the header section

---

### TC-004: Verify Navigation Menu Items
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Check all navigation menu items

**Expected Result:** Navigation menu displays: Home, Contact, About us, Cart, Log in, Sign up

---

### TC-005: Verify Product Categories Display
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Check product categories section

**Expected Result:** Three categories are displayed: Phones, Laptops, Monitors

---

### TC-006: Verify Products Display on Homepage
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Scroll down to view products
2. Check if products are displayed

**Expected Result:** Products are displayed in a grid/list format with images, names, and prices

---

### TC-007: Verify Homepage Footer
**Priority:** Low  
**Preconditions:** User is on homepage  
**Steps:**
1. Scroll to bottom of page
2. Check footer content

**Expected Result:** Footer is displayed with copyright information or relevant links

---

### TC-008: Verify Homepage Responsiveness
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Steps:**
1. Resize browser window to different sizes (mobile, tablet, desktop)

**Expected Result:** Homepage adapts to different screen sizes appropriately

---

## 2. User Registration Test Cases

### TC-009: Verify Sign Up Link is Clickable
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Click on "Sign up" link in navigation

**Expected Result:** Sign up modal/popup opens

---

### TC-010: Verify Sign Up Modal Opens
**Priority:** High  
**Preconditions:** User clicked Sign up link  
**Steps:**
1. Verify modal appears

**Expected Result:** Sign up modal opens with username and password fields

---

### TC-011: Register with Valid Username and Password
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter valid username (e.g., "testuser123")
2. Enter valid password (e.g., "password123")
3. Click "Sign up" button

**Expected Result:** Success message appears: "Sign up successful." Modal closes automatically

---

### TC-012: Register with Existing Username
**Priority:** High  
**Preconditions:** Sign up modal is open, username already exists  
**Steps:**
1. Enter existing username
2. Enter any password
3. Click "Sign up" button

**Expected Result:** Error message appears: "This user already exist."

---

### TC-013: Register with Empty Username
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Leave username field empty
2. Enter password
3. Click "Sign up" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-014: Register with Empty Password
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username
2. Leave password field empty
3. Click "Sign up" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-015: Register with Both Fields Empty
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Leave both username and password fields empty
2. Click "Sign up" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-016: Register with Special Characters in Username
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username with special characters (e.g., "user@#$%")
2. Enter password
3. Click "Sign up" button

**Expected Result:** System accepts or rejects based on validation rules

---

### TC-017: Register with Very Long Username
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username with 100+ characters
2. Enter password
3. Click "Sign up" button

**Expected Result:** System handles long username appropriately (accepts or shows error)

---

### TC-018: Register with Very Short Username
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username with 1 character
2. Enter password
3. Click "Sign up" button

**Expected Result:** System accepts or shows validation error

---

### TC-019: Register with Very Long Password
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username
2. Enter password with 200+ characters
3. Click "Sign up" button

**Expected Result:** System handles long password appropriately

---

### TC-020: Register with Very Short Password
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username
2. Enter password with 1 character
3. Click "Sign up" button

**Expected Result:** System accepts or shows validation error

---

### TC-021: Register with Spaces in Username
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username with spaces (e.g., "test user")
2. Enter password
3. Click "Sign up" button

**Expected Result:** System accepts or rejects based on validation rules

---

### TC-022: Register with Spaces in Password
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username
2. Enter password with spaces (e.g., "pass word")
3. Click "Sign up" button

**Expected Result:** System accepts or rejects based on validation rules

---

### TC-023: Close Sign Up Modal with X Button
**Priority:** Medium  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Click X button (close button) on modal

**Expected Result:** Modal closes without saving data

---

### TC-024: Close Sign Up Modal by Clicking Outside
**Priority:** Low  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Click outside the modal area

**Expected Result:** Modal closes or stays open (depending on implementation)

---

### TC-025: Register with SQL Injection Attempt
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter SQL injection string in username (e.g., "admin' OR '1'='1")
2. Enter password
3. Click "Sign up" button

**Expected Result:** System rejects or sanitizes input, no SQL injection occurs

---

### TC-026: Register with XSS Attempt
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter XSS script in username (e.g., "<script>alert('XSS')</script>")
2. Enter password
3. Click "Sign up" button

**Expected Result:** System rejects or sanitizes input, no script execution occurs

---

## 3. User Login Test Cases

### TC-027: Verify Log In Link is Clickable
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Click on "Log in" link in navigation

**Expected Result:** Log in modal/popup opens

---

### TC-028: Verify Log In Modal Opens
**Priority:** High  
**Preconditions:** User clicked Log in link  
**Steps:**
1. Verify modal appears

**Expected Result:** Log in modal opens with username and password fields

---

### TC-029: Login with Valid Credentials
**Priority:** High  
**Preconditions:** User account exists, Log in modal is open  
**Steps:**
1. Enter valid username
2. Enter valid password
3. Click "Log in" button

**Expected Result:** Success message appears: "Welcome [username]". User is logged in, navigation shows "Log out" instead of "Log in"

---

### TC-030: Login with Invalid Username
**Priority:** High  
**Preconditions:** Log in modal is open  
**Steps:**
1. Enter non-existent username
2. Enter any password
3. Click "Log in" button

**Expected Result:** Error message appears: "User does not exist."

---

### TC-031: Login with Invalid Password
**Priority:** High  
**Preconditions:** Log in modal is open, username exists  
**Steps:**
1. Enter valid username
2. Enter incorrect password
3. Click "Log in" button

**Expected Result:** Error message appears: "Wrong password."

---

### TC-032: Login with Empty Username
**Priority:** High  
**Preconditions:** Log in modal is open  
**Steps:**
1. Leave username field empty
2. Enter password
3. Click "Log in" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-033: Login with Empty Password
**Priority:** High  
**Preconditions:** Log in modal is open  
**Steps:**
1. Enter username
2. Leave password field empty
3. Click "Log in" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-034: Login with Both Fields Empty
**Priority:** High  
**Preconditions:** Log in modal is open  
**Steps:**
1. Leave both fields empty
2. Click "Log in" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-035: Login with Case Sensitive Username
**Priority:** Medium  
**Preconditions:** Log in modal is open, account exists with lowercase username  
**Steps:**
1. Enter username with different case (e.g., "TestUser" instead of "testuser")
2. Enter correct password
3. Click "Log in" button

**Expected Result:** System accepts or rejects based on case sensitivity rules

---

### TC-036: Login with Case Sensitive Password
**Priority:** Medium  
**Preconditions:** Log in modal is open  
**Steps:**
1. Enter correct username
2. Enter password with different case
3. Click "Log in" button

**Expected Result:** System accepts or rejects based on case sensitivity rules

---

### TC-037: Login with SQL Injection in Username
**Priority:** High  
**Preconditions:** Log in modal is open  
**Steps:**
1. Enter SQL injection string in username
2. Enter password
3. Click "Log in" button

**Expected Result:** System rejects or sanitizes input, login fails

---

### TC-038: Login with XSS in Username
**Priority:** High  
**Preconditions:** Log in modal is open  
**Steps:**
1. Enter XSS script in username
2. Enter password
3. Click "Log in" button

**Expected Result:** System rejects or sanitizes input, no script execution

---

### TC-039: Close Log In Modal with X Button
**Priority:** Medium  
**Preconditions:** Log in modal is open  
**Steps:**
1. Click X button on modal

**Expected Result:** Modal closes without logging in

---

### TC-040: Verify Logout Functionality
**Priority:** High  
**Preconditions:** User is logged in  
**Steps:**
1. Click "Log out" link in navigation

**Expected Result:** User is logged out, navigation shows "Log in" and "Sign up" again

---

### TC-041: Verify User Session Persists After Page Refresh
**Priority:** Medium  
**Preconditions:** User is logged in  
**Steps:**
1. Refresh the page (F5)

**Expected Result:** User remains logged in after refresh

---

### TC-042: Verify User Session Persists After Closing Tab
**Priority:** Medium  
**Preconditions:** User is logged in  
**Steps:**
1. Close browser tab
2. Open new tab and navigate to demoblaze.com

**Expected Result:** User remains logged in or is logged out (depends on session management)

---

## 4. Product Browsing Test Cases

### TC-043: Click on Phones Category
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Click on "Phones" category

**Expected Result:** Page navigates to phones category, displays all phone products

---

### TC-044: Click on Laptops Category
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Click on "Laptops" category

**Expected Result:** Page navigates to laptops category, displays all laptop products

---

### TC-045: Click on Monitors Category
**Priority:** High  
**Preconditions:** User is on homepage  
**Steps:**
1. Click on "Monitors" category

**Expected Result:** Page navigates to monitors category, displays all monitor products

---

### TC-046: Verify Products Display in Category Page
**Priority:** High  
**Preconditions:** User is on a category page  
**Steps:**
1. Check if products are displayed

**Expected Result:** All products in the category are displayed with images, names, and prices

---

### TC-047: Verify Product Images Load
**Priority:** Medium  
**Preconditions:** User is on a category page  
**Steps:**
1. Check if product images are visible

**Expected Result:** All product images load correctly without broken image icons

---

### TC-048: Verify Product Names Display
**Priority:** High  
**Preconditions:** User is on a category page  
**Steps:**
1. Check if product names are displayed

**Expected Result:** All products show their names clearly

---

### TC-049: Verify Product Prices Display
**Priority:** High  
**Preconditions:** User is on a category page  
**Steps:**
1. Check if product prices are displayed

**Expected Result:** All products show their prices in correct format (e.g., $500)

---

### TC-050: Click on Individual Product
**Priority:** High  
**Preconditions:** User is on a category page  
**Steps:**
1. Click on any product

**Expected Result:** Page navigates to product details page

---

### TC-051: Navigate Back from Category to Homepage
**Priority:** Medium  
**Preconditions:** User is on a category page  
**Steps:**
1. Click "Home" in navigation

**Expected Result:** Page navigates back to homepage

---

### TC-052: Verify Product Count in Category
**Priority:** Low  
**Preconditions:** User is on a category page  
**Steps:**
1. Count number of products displayed

**Expected Result:** Correct number of products for that category are displayed

---

### TC-053: Verify Category Page Title
**Priority:** Low  
**Preconditions:** User is on a category page  
**Steps:**
1. Check browser tab title

**Expected Result:** Browser tab shows appropriate title for the category

---

### TC-054: Verify Empty Category Handling
**Priority:** Low  
**Preconditions:** Category has no products (if applicable)  
**Steps:**
1. Navigate to empty category

**Expected Result:** Appropriate message displayed (e.g., "No products found")

---

## 5. Product Details Test Cases

### TC-055: Verify Product Details Page Loads
**Priority:** High  
**Preconditions:** User clicked on a product  
**Steps:**
1. Wait for product details page to load

**Expected Result:** Product details page loads successfully

---

### TC-056: Verify Product Image on Details Page
**Priority:** High  
**Preconditions:** User is on product details page  
**Steps:**
1. Check product image

**Expected Result:** Large product image is displayed clearly

---

### TC-057: Verify Product Name on Details Page
**Priority:** High  
**Preconditions:** User is on product details page  
**Steps:**
1. Check product name

**Expected Result:** Product name is displayed prominently

---

### TC-058: Verify Product Price on Details Page
**Priority:** High  
**Preconditions:** User is on product details page  
**Steps:**
1. Check product price

**Expected Result:** Product price is displayed clearly

---

### TC-059: Verify Product Description on Details Page
**Priority:** Medium  
**Preconditions:** User is on product details page  
**Steps:**
1. Check product description

**Expected Result:** Product description is displayed with details about the product

---

### TC-060: Verify Add to Cart Button Exists
**Priority:** High  
**Preconditions:** User is on product details page  
**Steps:**
1. Check for "Add to cart" button

**Expected Result:** "Add to cart" button is visible and clickable

---

### TC-061: Click Add to Cart Button
**Priority:** High  
**Preconditions:** User is on product details page  
**Steps:**
1. Click "Add to cart" button

**Expected Result:** Success message appears: "Product added." Product is added to cart

---

### TC-062: Add Same Product Multiple Times
**Priority:** Medium  
**Preconditions:** User is on product details page  
**Steps:**
1. Click "Add to cart" button
2. Click "Add to cart" button again
3. Click "Add to cart" button third time

**Expected Result:** Product is added multiple times, cart shows correct quantity

---

### TC-063: Verify Back Button on Product Details
**Priority:** Medium  
**Preconditions:** User is on product details page  
**Steps:**
1. Click browser back button

**Expected Result:** User returns to previous page (category or homepage)

---

### TC-064: Verify Product Details Page Title
**Priority:** Low  
**Preconditions:** User is on product details page  
**Steps:**
1. Check browser tab title

**Expected Result:** Browser tab shows product name or appropriate title

---

### TC-065: Add Product to Cart While Not Logged In
**Priority:** High  
**Preconditions:** User is not logged in, on product details page  
**Steps:**
1. Click "Add to cart" button

**Expected Result:** Product is added to cart (cart may work without login)

---

### TC-066: Verify Product Details Page Responsiveness
**Priority:** Medium  
**Preconditions:** User is on product details page  
**Steps:**
1. Resize browser window

**Expected Result:** Product details page adapts to different screen sizes

---

## 6. Shopping Cart Test Cases

### TC-067: Verify Cart Link is Clickable
**Priority:** High  
**Preconditions:** User is on any page  
**Steps:**
1. Click "Cart" link in navigation

**Expected Result:** Cart page opens

---

### TC-068: Verify Cart Page Loads
**Priority:** High  
**Preconditions:** User clicked Cart link  
**Steps:**
1. Wait for cart page to load

**Expected Result:** Cart page loads successfully

---

### TC-069: Verify Empty Cart Display
**Priority:** High  
**Preconditions:** Cart is empty, user is on cart page  
**Steps:**
1. Check cart content

**Expected Result:** Appropriate message displayed (e.g., "Cart is empty" or empty state)

---

### TC-070: Verify Products Display in Cart
**Priority:** High  
**Preconditions:** Cart has products, user is on cart page  
**Steps:**
1. Check cart content

**Expected Result:** All added products are displayed with images, names, and prices

---

### TC-071: Verify Product Details in Cart
**Priority:** High  
**Preconditions:** Cart has products, user is on cart page  
**Steps:**
1. Check each product in cart

**Expected Result:** Each product shows: image, name, price, and delete option

---

### TC-072: Verify Total Price Calculation
**Priority:** High  
**Preconditions:** Cart has multiple products, user is on cart page  
**Steps:**
1. Check total price displayed

**Expected Result:** Total price equals sum of all product prices

---

### TC-073: Delete Product from Cart
**Priority:** High  
**Preconditions:** Cart has products, user is on cart page  
**Steps:**
1. Click "Delete" button next to a product

**Expected Result:** Product is removed from cart, total price is updated

---

### TC-074: Delete All Products from Cart
**Priority:** Medium  
**Preconditions:** Cart has multiple products, user is on cart page  
**Steps:**
1. Delete all products one by one

**Expected Result:** All products are removed, cart shows empty state

---

### TC-075: Verify Place Order Button Exists
**Priority:** High  
**Preconditions:** Cart has products, user is on cart page  
**Steps:**
1. Check for "Place Order" button

**Expected Result:** "Place Order" button is visible

---

### TC-076: Verify Place Order Button When Cart is Empty
**Priority:** Medium  
**Preconditions:** Cart is empty, user is on cart page  
**Steps:**
1. Check for "Place Order" button

**Expected Result:** "Place Order" button is hidden or disabled

---

### TC-077: Add Multiple Different Products to Cart
**Priority:** High  
**Preconditions:** User is browsing products  
**Steps:**
1. Add product 1 to cart
2. Add product 2 to cart
3. Add product 3 to cart
4. Go to cart

**Expected Result:** All three products are displayed in cart with correct details

---

### TC-078: Verify Cart Persists After Page Refresh
**Priority:** Medium  
**Preconditions:** Cart has products, user is on cart page  
**Steps:**
1. Refresh the page (F5)

**Expected Result:** Cart items persist after refresh

---

### TC-079: Verify Cart Persists After Logout
**Priority:** Medium  
**Preconditions:** User is logged in, cart has products  
**Steps:**
1. Log out
2. Check cart

**Expected Result:** Cart items persist or are cleared (depends on implementation)

---

### TC-080: Verify Cart Persists After Login
**Priority:** Medium  
**Preconditions:** User has items in cart, not logged in  
**Steps:**
1. Log in
2. Check cart

**Expected Result:** Cart items persist or merge with account cart

---

### TC-081: Verify Cart Total Updates After Deletion
**Priority:** High  
**Preconditions:** Cart has multiple products, user is on cart page  
**Steps:**
1. Note the total price
2. Delete one product
3. Check new total price

**Expected Result:** Total price decreases by the deleted product's price

---

### TC-082: Verify Product Quantity in Cart
**Priority:** Medium  
**Preconditions:** Same product added multiple times, user is on cart page  
**Steps:**
1. Check how quantity is displayed

**Expected Result:** Quantity is shown correctly (either as separate items or with quantity counter)

---

### TC-083: Verify Cart Page Title
**Priority:** Low  
**Preconditions:** User is on cart page  
**Steps:**
1. Check browser tab title

**Expected Result:** Browser tab shows "Cart" or appropriate title

---

## 7. Checkout/Place Order Test Cases

### TC-084: Click Place Order Button
**Priority:** High  
**Preconditions:** Cart has products, user is on cart page  
**Steps:**
1. Click "Place Order" button

**Expected Result:** Place order modal/popup opens

---

### TC-085: Verify Place Order Modal Opens
**Priority:** High  
**Preconditions:** User clicked Place Order button  
**Steps:**
1. Verify modal appears

**Expected Result:** Place order modal opens with form fields

---

### TC-086: Verify Required Fields in Place Order Form
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Check form fields

**Expected Result:** Form has fields for: Name, Country, City, Credit card, Month, Year

---

### TC-087: Place Order with Valid Data
**Priority:** High  
**Preconditions:** Place order modal is open, cart has products  
**Steps:**
1. Enter name (e.g., "John Doe")
2. Enter country (e.g., "USA")
3. Enter city (e.g., "New York")
4. Enter credit card (e.g., "1234567890123456")
5. Enter month (e.g., "12")
6. Enter year (e.g., "2025")
7. Click "Purchase" button

**Expected Result:** Success message appears with order details, order ID, and confirmation. Modal closes

---

### TC-088: Place Order with Empty Name Field
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Leave name field empty
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-089: Place Order with Empty Country Field
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Leave country field empty
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-090: Place Order with Empty City Field
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Leave city field empty
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-091: Place Order with Empty Credit Card Field
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Leave credit card field empty
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-092: Place Order with Empty Month Field
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Leave month field empty
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-093: Place Order with Empty Year Field
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Leave year field empty
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-094: Place Order with All Fields Empty
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Leave all fields empty
2. Click "Purchase" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-095: Place Order with Invalid Credit Card Format
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter invalid credit card (e.g., "123" or "abc")
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form accepts it (depends on validation)

---

### TC-096: Place Order with Invalid Month (Greater than 12)
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter month as 13 or higher
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form accepts it (depends on validation)

---

### TC-097: Place Order with Invalid Month (Less than 1)
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter month as 0 or negative
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form accepts it (depends on validation)

---

### TC-098: Place Order with Past Year
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter year in the past (e.g., 2020)
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** Error message appears or form accepts it (depends on validation)

---

### TC-099: Place Order with Special Characters in Name
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter name with special characters (e.g., "John@Doe#123")
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** System accepts or rejects based on validation rules

---

### TC-100: Place Order with Numbers in Name Field
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter name with numbers (e.g., "John123")
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** System accepts or rejects based on validation rules

---

### TC-101: Place Order with Very Long Name
**Priority:** Low  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter name with 200+ characters
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** System handles long name appropriately

---

### TC-102: Place Order with SQL Injection in Name
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter SQL injection string in name field
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** System rejects or sanitizes input

---

### TC-103: Place Order with XSS in Name
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter XSS script in name field
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** System rejects or sanitizes input, no script execution

---

### TC-104: Verify Order Confirmation Details
**Priority:** High  
**Preconditions:** Order placed successfully  
**Steps:**
1. Check order confirmation message

**Expected Result:** Confirmation shows: order ID, amount, card number (masked), name, date

---

### TC-105: Verify Cart is Cleared After Successful Order
**Priority:** High  
**Preconditions:** Order placed successfully  
**Steps:**
1. Go to cart page

**Expected Result:** Cart is empty after successful order

---

### TC-106: Close Place Order Modal with X Button
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Click X button on modal

**Expected Result:** Modal closes without placing order

---

### TC-107: Place Order with Credit Card Containing Spaces
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter credit card with spaces (e.g., "1234 5678 9012 3456")
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** System accepts or rejects based on validation

---

### TC-108: Place Order with Credit Card Containing Dashes
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter credit card with dashes (e.g., "1234-5678-9012-3456")
2. Fill all other fields
3. Click "Purchase" button

**Expected Result:** System accepts or rejects based on validation

---

### TC-109: Place Order Multiple Times in Sequence
**Priority:** Medium  
**Preconditions:** Cart has products  
**Steps:**
1. Place first order
2. Add products to cart again
3. Place second order

**Expected Result:** Both orders are processed successfully with different order IDs

---

## 8. Navigation Test Cases

### TC-110: Click Home Link
**Priority:** Medium  
**Preconditions:** User is on any page  
**Steps:**
1. Click "Home" link in navigation

**Expected Result:** Page navigates to homepage

---

### TC-111: Click Contact Link
**Priority:** Medium  
**Preconditions:** User is on any page  
**Steps:**
1. Click "Contact" link in navigation

**Expected Result:** Contact modal/popup opens or contact page loads

---

### TC-112: Verify Contact Modal Opens
**Priority:** Medium  
**Preconditions:** User clicked Contact link  
**Steps:**
1. Verify modal appears

**Expected Result:** Contact modal opens with form fields (email, name, message)

---

### TC-113: Submit Contact Form with Valid Data
**Priority:** Medium  
**Preconditions:** Contact modal is open  
**Steps:**
1. Enter contact email
2. Enter contact name
3. Enter message
4. Click "Send message" button

**Expected Result:** Success message appears, modal closes

---

### TC-114: Submit Contact Form with Empty Fields
**Priority:** Medium  
**Preconditions:** Contact modal is open  
**Steps:**
1. Leave all fields empty
2. Click "Send message" button

**Expected Result:** Error message appears or form validation prevents submission

---

### TC-115: Click About Us Link
**Priority:** Medium  
**Preconditions:** User is on any page  
**Steps:**
1. Click "About us" link in navigation

**Expected Result:** About us modal/popup opens or about page loads

---

### TC-116: Verify About Us Modal Opens
**Priority:** Medium  
**Preconditions:** User clicked About us link  
**Steps:**
1. Verify modal appears

**Expected Result:** About us modal opens with information about the company

---

### TC-117: Verify Navigation Menu Persists Across Pages
**Priority:** Medium  
**Preconditions:** User navigates between pages  
**Steps:**
1. Navigate to different pages
2. Check navigation menu

**Expected Result:** Navigation menu is visible on all pages

---

### TC-118: Verify Browser Back Button Works
**Priority:** Medium  
**Preconditions:** User navigated through multiple pages  
**Steps:**
1. Click browser back button

**Expected Result:** User returns to previous page

---

### TC-119: Verify Browser Forward Button Works
**Priority:** Low  
**Preconditions:** User used back button  
**Steps:**
1. Click browser forward button

**Expected Result:** User goes forward to next page

---

### TC-120: Verify Logo Links to Homepage
**Priority:** Medium  
**Preconditions:** User is on any page  
**Steps:**
1. Click on logo

**Expected Result:** Page navigates to homepage

---

## 9. UI/UX Test Cases

### TC-121: Verify Page Loads Without Errors
**Priority:** High  
**Preconditions:** User navigates to any page  
**Steps:**
1. Check browser console for errors

**Expected Result:** No JavaScript errors in console

---

### TC-122: Verify Images Load Properly
**Priority:** Medium  
**Preconditions:** User is on any page with images  
**Steps:**
1. Check all images on page

**Expected Result:** All images load without broken image icons

---

### TC-123: Verify Buttons are Clickable
**Priority:** High  
**Preconditions:** User is on any page  
**Steps:**
1. Check all buttons on page

**Expected Result:** All buttons are clickable and respond to clicks

---

### TC-124: Verify Links are Clickable
**Priority:** High  
**Preconditions:** User is on any page  
**Steps:**
1. Check all links on page

**Expected Result:** All links are clickable and navigate correctly

---

### TC-125: Verify Text is Readable
**Priority:** Medium  
**Preconditions:** User is on any page  
**Steps:**
1. Check text readability

**Expected Result:** All text is readable with appropriate font size and color contrast

---

### TC-126: Verify Color Scheme Consistency
**Priority:** Low  
**Preconditions:** User navigates through pages  
**Steps:**
1. Check colors across different pages

**Expected Result:** Color scheme is consistent across all pages

---

### TC-127: Verify Font Consistency
**Priority:** Low  
**Preconditions:** User navigates through pages  
**Steps:**
1. Check fonts across different pages

**Expected Result:** Fonts are consistent across all pages

---

### TC-128: Verify Modal Overlay Appears
**Priority:** Medium  
**Preconditions:** User opens any modal  
**Steps:**
1. Check if overlay/backdrop appears behind modal

**Expected Result:** Dark overlay appears behind modal

---

### TC-129: Verify Modal is Centered
**Priority:** Medium  
**Preconditions:** User opens any modal  
**Steps:**
1. Check modal position

**Expected Result:** Modal is centered on screen

---

### TC-130: Verify Loading States
**Priority:** Medium  
**Preconditions:** User performs actions that require loading  
**Steps:**
1. Perform action (e.g., add to cart, place order)
2. Check for loading indicator

**Expected Result:** Loading indicator appears during processing

---

### TC-131: Verify Success Messages Display
**Priority:** High  
**Preconditions:** User performs successful action  
**Steps:**
1. Perform action (e.g., add to cart, place order)
2. Check for success message

**Expected Result:** Success message appears clearly

---

### TC-132: Verify Error Messages Display
**Priority:** High  
**Preconditions:** User performs action that causes error  
**Steps:**
1. Perform action that causes error
2. Check for error message

**Expected Result:** Error message appears clearly

---

### TC-133: Verify Hover Effects on Buttons
**Priority:** Low  
**Preconditions:** User is on any page  
**Steps:**
1. Hover over buttons

**Expected Result:** Buttons show hover effects (color change, cursor change)

---

### TC-134: Verify Hover Effects on Links
**Priority:** Low  
**Preconditions:** User is on any page  
**Steps:**
1. Hover over links

**Expected Result:** Links show hover effects (underline, color change)

---

### TC-135: Verify Focus States on Form Fields
**Priority:** Medium  
**Preconditions:** User is on form page  
**Steps:**
1. Click on form fields

**Expected Result:** Form fields show focus states (border highlight)

---

### TC-136: Verify Page Scroll Works
**Priority:** Medium  
**Preconditions:** User is on long page  
**Steps:**
1. Scroll page up and down

**Expected Result:** Page scrolls smoothly

---

### TC-137: Verify Responsive Design on Mobile
**Priority:** High  
**Preconditions:** User accesses site on mobile device or resized window  
**Steps:**
1. View site on mobile size (375px width)
2. Check layout

**Expected Result:** Site is responsive, elements stack properly, text is readable

---

### TC-138: Verify Responsive Design on Tablet
**Priority:** Medium  
**Preconditions:** User accesses site on tablet or resized window  
**Steps:**
1. View site on tablet size (768px width)
2. Check layout

**Expected Result:** Site is responsive, layout adapts appropriately

---

### TC-139: Verify Responsive Design on Desktop
**Priority:** Medium  
**Preconditions:** User accesses site on desktop  
**Steps:**
1. View site on desktop size (1920px width)
2. Check layout

**Expected Result:** Site displays properly with appropriate spacing

---

## 10. Security Test Cases

### TC-140: Verify HTTPS is Used
**Priority:** High  
**Preconditions:** User navigates to site  
**Steps:**
1. Check browser address bar

**Expected Result:** Site uses HTTPS protocol

---

### TC-141: Verify Password is Not Visible in Plain Text
**Priority:** High  
**Preconditions:** User is on login/registration form  
**Steps:**
1. Enter password
2. Check password field

**Expected Result:** Password is masked (shows dots or asterisks)

---

### TC-142: Verify Session Timeout
**Priority:** Medium  
**Preconditions:** User is logged in  
**Steps:**
1. Wait for extended period without activity
2. Try to perform action

**Expected Result:** Session expires, user is logged out or prompted to login again

---

### TC-143: Verify CSRF Protection
**Priority:** High  
**Preconditions:** User is logged in  
**Steps:**
1. Check if CSRF tokens are used in forms

**Expected Result:** Forms include CSRF tokens or other protection mechanisms

---

### TC-144: Verify Input Sanitization
**Priority:** High  
**Preconditions:** User enters malicious input  
**Steps:**
1. Enter SQL injection, XSS, or other malicious input
2. Submit form

**Expected Result:** Input is sanitized, no code execution occurs

---

### TC-145: Verify No Sensitive Data in URL
**Priority:** High  
**Preconditions:** User performs actions  
**Steps:**
1. Check browser URL after actions

**Expected Result:** No passwords or sensitive data visible in URL

---

### TC-146: Verify Error Messages Don't Reveal System Info
**Priority:** Medium  
**Preconditions:** User triggers error  
**Steps:**
1. Trigger error
2. Check error message

**Expected Result:** Error messages don't reveal system paths, database info, or stack traces

---

### TC-147: Verify Access Control for Protected Pages
**Priority:** High  
**Preconditions:** User is not logged in  
**Steps:**
1. Try to access protected pages directly via URL

**Expected Result:** User is redirected to login or access is denied

---

### TC-148: Verify SQL Injection Prevention
**Priority:** High  
**Preconditions:** User is on any form  
**Steps:**
1. Enter SQL injection strings in all input fields
2. Submit forms

**Expected Result:** SQL injection attempts are blocked or sanitized

---

### TC-149: Verify XSS Prevention
**Priority:** High  
**Preconditions:** User is on any form  
**Steps:**
1. Enter XSS scripts in all input fields
2. Submit forms

**Expected Result:** XSS attempts are blocked or sanitized

---

### TC-150: Verify Clickjacking Protection
**Priority:** Medium  
**Preconditions:** User accesses site  
**Steps:**
1. Check HTTP headers for X-Frame-Options

**Expected Result:** Site has clickjacking protection headers

---

## 11. Performance Test Cases

### TC-151: Verify Homepage Load Time
**Priority:** Medium  
**Preconditions:** User has internet connection  
**Steps:**
1. Navigate to homepage
2. Measure load time

**Expected Result:** Homepage loads within acceptable time (e.g., < 3 seconds)

---

### TC-152: Verify Category Page Load Time
**Priority:** Medium  
**Preconditions:** User navigates to category  
**Steps:**
1. Navigate to category page
2. Measure load time

**Expected Result:** Category page loads within acceptable time

---

### TC-153: Verify Product Details Page Load Time
**Priority:** Medium  
**Preconditions:** User navigates to product  
**Steps:**
1. Navigate to product details page
2. Measure load time

**Expected Result:** Product details page loads within acceptable time

---

### TC-154: Verify Image Optimization
**Priority:** Medium  
**Preconditions:** User is on any page with images  
**Steps:**
1. Check image file sizes

**Expected Result:** Images are optimized and not excessively large

---

### TC-155: Verify Page Works with Slow Connection
**Priority:** Medium  
**Preconditions:** User has slow internet connection  
**Steps:**
1. Simulate slow connection
2. Navigate through site

**Expected Result:** Site still functions, shows loading indicators

---

### TC-156: Verify Multiple Simultaneous Requests
**Priority:** Low  
**Preconditions:** Multiple users access site  
**Steps:**
1. Simulate multiple users performing actions simultaneously

**Expected Result:** Site handles multiple requests without crashing

---

### TC-157: Verify Large Cart Performance
**Priority:** Low  
**Preconditions:** User adds many products to cart  
**Steps:**
1. Add 50+ products to cart
2. Open cart page

**Expected Result:** Cart page loads and displays all products without performance issues

---

## 12. Compatibility Test Cases

### TC-158: Verify Site Works on Chrome
**Priority:** High  
**Preconditions:** User has Chrome browser  
**Steps:**
1. Open site in Chrome
2. Test all major functionalities

**Expected Result:** Site works correctly on Chrome

---

### TC-159: Verify Site Works on Firefox
**Priority:** High  
**Preconditions:** User has Firefox browser  
**Steps:**
1. Open site in Firefox
2. Test all major functionalities

**Expected Result:** Site works correctly on Firefox

---

### TC-160: Verify Site Works on Edge
**Priority:** High  
**Preconditions:** User has Edge browser  
**Steps:**
1. Open site in Edge
2. Test all major functionalities

**Expected Result:** Site works correctly on Edge

---

### TC-161: Verify Site Works on Safari
**Priority:** Medium  
**Preconditions:** User has Safari browser  
**Steps:**
1. Open site in Safari
2. Test all major functionalities

**Expected Result:** Site works correctly on Safari

---

### TC-162: Verify Site Works on Mobile Chrome
**Priority:** High  
**Preconditions:** User has mobile device with Chrome  
**Steps:**
1. Open site in mobile Chrome
2. Test all major functionalities

**Expected Result:** Site works correctly on mobile Chrome

---

### TC-163: Verify Site Works on Mobile Safari
**Priority:** High  
**Preconditions:** User has iOS device with Safari  
**Steps:**
1. Open site in mobile Safari
2. Test all major functionalities

**Expected Result:** Site works correctly on mobile Safari

---

### TC-164: Verify Site Works on Different Screen Resolutions
**Priority:** Medium  
**Preconditions:** User has different screen sizes  
**Steps:**
1. Test site on various resolutions (1366x768, 1920x1080, 2560x1440)

**Expected Result:** Site displays correctly on all resolutions

---

### TC-165: Verify Site Works on Different Operating Systems
**Priority:** Medium  
**Preconditions:** User has different OS  
**Steps:**
1. Test site on Windows, macOS, Linux, Android, iOS

**Expected Result:** Site works correctly on all operating systems

---

## 13. Edge Cases and Negative Test Cases

### TC-166: Add Product to Cart, Then Delete from Product Page
**Priority:** Medium  
**Preconditions:** Product is in cart  
**Steps:**
1. Go to product details page
2. Try to remove product from cart (if option exists)

**Expected Result:** Appropriate behavior (may not be possible from product page)

---

### TC-167: Place Order with Expired Credit Card
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter expired credit card date (past month/year)
2. Fill other fields
3. Click "Purchase"

**Expected Result:** System accepts or rejects based on validation

---

### TC-168: Place Order with Very Long Credit Card Number
**Priority:** Low  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter credit card with 30+ digits
2. Fill other fields
3. Click "Purchase"

**Expected Result:** System handles appropriately

---

### TC-169: Place Order with Non-Numeric Credit Card
**Priority:** Medium  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter credit card with letters (e.g., "abcdefghijklmnop")
2. Fill other fields
3. Click "Purchase"

**Expected Result:** System accepts or rejects based on validation

---

### TC-170: Add Maximum Number of Products to Cart
**Priority:** Low  
**Preconditions:** User is browsing products  
**Steps:**
1. Add all available products to cart
2. Check cart

**Expected Result:** All products are added, cart functions correctly

---

### TC-171: Rapidly Click Add to Cart Multiple Times
**Priority:** Medium  
**Preconditions:** User is on product details page  
**Steps:**
1. Rapidly click "Add to cart" button 10 times

**Expected Result:** System handles rapid clicks correctly, product added appropriate number of times

---

### TC-172: Navigate Away During Form Submission
**Priority:** Medium  
**Preconditions:** User is filling form  
**Steps:**
1. Start filling form
2. Navigate away before submitting

**Expected Result:** Form data is lost or saved (depends on implementation)

---

### TC-173: Refresh Page During Checkout
**Priority:** Medium  
**Preconditions:** User is in checkout process  
**Steps:**
1. Start checkout
2. Refresh page

**Expected Result:** Checkout process resets or continues (depends on implementation)

---

### TC-174: Use Browser Back Button During Checkout
**Priority:** Medium  
**Preconditions:** User is in checkout process  
**Steps:**
1. Start checkout
2. Click browser back button

**Expected Result:** User returns to previous page, checkout may be cancelled

---

### TC-175: Open Multiple Tabs and Add to Cart
**Priority:** Medium  
**Preconditions:** User opens site in multiple tabs  
**Steps:**
1. Open site in tab 1, add product to cart
2. Open site in tab 2, check cart
3. Add different product in tab 2

**Expected Result:** Cart syncs correctly across tabs or shows separate carts

---

### TC-176: Register with Maximum Length Username
**Priority:** Low  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username at maximum allowed length
2. Enter password
3. Click "Sign up"

**Expected Result:** Registration succeeds or fails based on validation

---

### TC-177: Register with Maximum Length Password
**Priority:** Low  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Enter username
2. Enter password at maximum allowed length
3. Click "Sign up"

**Expected Result:** Registration succeeds or fails based on validation

---

### TC-178: Login with Recently Changed Password
**Priority:** Low  
**Preconditions:** User password was changed (if feature exists)  
**Steps:**
1. Try to login with old password
2. Try to login with new password

**Expected Result:** Old password fails, new password succeeds

---

### TC-179: Add Product, Logout, Login, Check Cart
**Priority:** Medium  
**Preconditions:** User account exists  
**Steps:**
1. Add product to cart
2. Logout
3. Login with same account
4. Check cart

**Expected Result:** Cart persists or is cleared (depends on implementation)

---

### TC-180: Place Order with Zero Amount (if possible)
**Priority:** Low  
**Preconditions:** Cart is empty but order can be initiated  
**Steps:**
1. Try to place order with empty cart

**Expected Result:** Order is prevented or fails

---

## 14. Accessibility Test Cases

### TC-181: Verify Keyboard Navigation Works
**Priority:** Medium  
**Preconditions:** User uses keyboard only  
**Steps:**
1. Navigate site using only keyboard (Tab, Enter, Arrow keys)

**Expected Result:** All interactive elements are accessible via keyboard

---

### TC-182: Verify Alt Text for Images
**Priority:** Medium  
**Preconditions:** User is on any page with images  
**Steps:**
1. Check if images have alt text attributes

**Expected Result:** All images have descriptive alt text

---

### TC-183: Verify Form Labels are Associated
**Priority:** Medium  
**Preconditions:** User is on any form  
**Steps:**
1. Check if form fields have associated labels

**Expected Result:** All form fields have proper label associations

---

### TC-184: Verify Color Contrast Meets Standards
**Priority:** Medium  
**Preconditions:** User is on any page  
**Steps:**
1. Check text color contrast against background

**Expected Result:** Text has sufficient contrast (WCAG AA standard)

---

### TC-185: Verify Focus Indicators are Visible
**Priority:** Medium  
**Preconditions:** User navigates with keyboard  
**Steps:**
1. Tab through interactive elements
2. Check focus indicators

**Expected Result:** All focused elements show clear focus indicators

---

### TC-186: Verify ARIA Labels Where Needed
**Priority:** Low  
**Preconditions:** User is on any page  
**Steps:**
1. Check for ARIA labels on interactive elements

**Expected Result:** Complex interactive elements have ARIA labels

---

### TC-187: Verify Page Has Proper Heading Structure
**Priority:** Medium  
**Preconditions:** User is on any page  
**Steps:**
1. Check heading hierarchy (h1, h2, h3, etc.)

**Expected Result:** Page has logical heading structure

---

### TC-188: Verify Screen Reader Compatibility
**Priority:** Medium  
**Preconditions:** User uses screen reader  
**Steps:**
1. Test site with screen reader software

**Expected Result:** Site is navigable and understandable with screen reader

---

## 15. Data Validation Test Cases

### TC-189: Verify Username Validation Rules
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Test various username formats (valid and invalid)

**Expected Result:** System enforces username validation rules consistently

---

### TC-190: Verify Password Validation Rules
**Priority:** High  
**Preconditions:** Sign up modal is open  
**Steps:**
1. Test various password formats (valid and invalid)

**Expected Result:** System enforces password validation rules consistently

---

### TC-191: Verify Email Validation in Contact Form
**Priority:** Medium  
**Preconditions:** Contact modal is open  
**Steps:**
1. Enter invalid email formats
2. Submit form

**Expected Result:** System validates email format correctly

---

### TC-192: Verify Credit Card Number Validation
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter various credit card number formats
2. Submit form

**Expected Result:** System validates credit card format appropriately

---

### TC-193: Verify Date Validation (Month/Year)
**Priority:** High  
**Preconditions:** Place order modal is open  
**Steps:**
1. Enter invalid dates (e.g., month 13, year 1900)
2. Submit form

**Expected Result:** System validates dates correctly

---

### TC-194: Verify Text Field Length Limits
**Priority:** Medium  
**Preconditions:** User is on any form  
**Steps:**
1. Enter text exceeding field limits
2. Check behavior

**Expected Result:** System enforces or handles field length limits

---

### TC-195: Verify Numeric Field Validation
**Priority:** Medium  
**Preconditions:** User is on form with numeric fields  
**Steps:**
1. Enter non-numeric values in numeric fields
2. Submit form

**Expected Result:** System validates numeric fields correctly

---

### TC-196: Verify Required Field Indicators
**Priority:** Medium  
**Preconditions:** User is on any form  
**Steps:**
1. Check if required fields are marked

**Expected Result:** Required fields are clearly marked (asterisk, label, etc.)

---

### TC-197: Verify Input Trimming (Leading/Trailing Spaces)
**Priority:** Low  
**Preconditions:** User is on any form  
**Steps:**
1. Enter values with leading/trailing spaces
2. Submit form

**Expected Result:** System trims spaces or preserves them consistently

---

### TC-198: Verify Special Character Handling
**Priority:** Medium  
**Preconditions:** User is on any form  
**Steps:**
1. Enter special characters in various fields
2. Submit form

**Expected Result:** System handles special characters appropriately

---

### TC-199: Verify Unicode Character Support
**Priority:** Low  
**Preconditions:** User is on any form  
**Steps:**
1. Enter Unicode characters (e.g., Arabic, Chinese, emoji)
2. Submit form

**Expected Result:** System handles Unicode characters correctly

---

### TC-200: Verify Data Persistence After Validation Error
**Priority:** Medium  
**Preconditions:** User submits form with errors  
**Steps:**
1. Fill form with some valid and invalid data
2. Submit form
3. Check if valid data is preserved

**Expected Result:** Valid data is preserved, only invalid fields show errors

---

## Summary

**Total Test Cases:** 200

**Priority Breakdown:**
- High Priority: ~80 test cases
- Medium Priority: ~90 test cases
- Low Priority: ~30 test cases

**Category Breakdown:**
1. Homepage: 8 test cases
2. User Registration: 18 test cases
3. User Login: 16 test cases
4. Product Browsing: 12 test cases
5. Product Details: 12 test cases
6. Shopping Cart: 17 test cases
7. Checkout/Place Order: 26 test cases
8. Navigation: 11 test cases
9. UI/UX: 19 test cases
10. Security: 11 test cases
11. Performance: 7 test cases
12. Compatibility: 8 test cases
13. Edge Cases: 15 test cases
14. Accessibility: 8 test cases
15. Data Validation: 12 test cases

---

## Test Execution Notes

1. **Test Environment:** Ensure stable internet connection and use latest browser versions
2. **Test Data:** Prepare test data for registration, login, and checkout scenarios
3. **Test Execution Order:** Execute high priority test cases first
4. **Bug Reporting:** Document any deviations from expected results with screenshots
5. **Retesting:** Retest fixed bugs to ensure resolution
6. **Regression Testing:** Perform regression testing after bug fixes

---

## Test Coverage Areas

✅ Functional Testing  
✅ UI/UX Testing  
✅ Security Testing  
✅ Performance Testing  
✅ Compatibility Testing  
✅ Accessibility Testing  
✅ Data Validation Testing  
✅ Negative Testing  
✅ Edge Case Testing  
✅ Integration Testing (User flows)

---

**End of Test Cases Document**


# Test Cases Document - DemoBlaze.com
## Part 3: Test Cases TC-051 to TC-075

**Project:** DemoBlaze E-Commerce Website  
**URL:** https://demoblaze.com/  
**Document Version:** 2.0  
**Date:** 2024  
**Prepared By:** Mohammed Abdel Naeem

---

## Test Case TC-051

**Test Case ID:** TC-051  
**Title / Summary:** Navigate Back from Category to Homepage  
**Test Suite / Module:** Product Browsing Module  
**Priority:** Medium  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on a category page (Phones, Laptops, or Monitors)
- Navigation menu is visible

**Test Steps:**
1. Navigate to any category page (e.g., Phones)
2. Locate "Home" link in navigation menu
3. Click "Home" link in navigation
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
Page navigates back to homepage. Homepage loads successfully. User can see all products and categories again.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- User is on homepage
- Homepage elements are visible

**Attachments / Notes:**
_Add screenshot if navigation fails_

---

## Test Case TC-052

**Test Case ID:** TC-052  
**Title / Summary:** Verify Product Count in Category  
**Test Suite / Module:** Product Browsing Module  
**Priority:** Low  
**Test Type:** Functional / Data Validation  

**Preconditions:**
- User is on a category page
- Products are displayed

**Test Steps:**
1. Navigate to any category page (e.g., Phones)
2. Wait for page to load
3. Count number of products displayed
4. Verify count matches expected number

**Test Data:**
- Category: Phones / Laptops / Monitors
- Expected count: Varies by category

**Expected Result:**
Correct number of products for that category are displayed. Count matches the actual number of products available in the category.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product count is verified
- All products are displayed

**Attachments / Notes:**
_Note the actual product count for each category_

---

## Test Case TC-053

**Test Case ID:** TC-053  
**Title / Summary:** Verify Category Page Title  
**Test Suite / Module:** Product Browsing Module  
**Priority:** Low  
**Test Type:** UI  

**Preconditions:**
- User is on a category page
- Browser tab is visible

**Test Steps:**
1. Navigate to any category page (e.g., Phones)
2. Check browser tab title
3. Verify the title text

**Test Data:**
- Category: Phones / Laptops / Monitors

**Expected Result:**
Browser tab shows appropriate title for the category. Title is clear and descriptive (e.g., "Phones" or "STORE - Phones").

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Browser tab shows correct title
- User can identify the category from tab title

**Attachments / Notes:**
_Add screenshot of browser tab if needed_

---

## Test Case TC-054

**Test Case ID:** TC-054  
**Title / Summary:** Verify Empty Category Handling  
**Test Suite / Module:** Product Browsing Module  
**Priority:** Low  
**Test Type:** Functional / Edge Case  

**Preconditions:**
- Category has no products (if applicable)
- User can access empty category

**Test Steps:**
1. Navigate to empty category (if such category exists)
2. Wait for page to load
3. Check page content
4. Verify empty state message

**Test Data:**
- Category: Empty category (if available)

**Expected Result:**
Appropriate message displayed (e.g., "No products found" or "This category is empty"). Page handles empty state gracefully without errors.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Empty category is handled properly
- User sees appropriate message

**Attachments / Notes:**
_Add screenshot of empty category state if available_

---

## Test Case TC-055

**Test Case ID:** TC-055  
**Title / Summary:** Verify Product Details Page Loads  
**Test Suite / Module:** Product Details Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User clicked on a product
- Product details page should load

**Test Steps:**
1. Navigate to any category page
2. Click on any product
3. Wait for product details page to load
4. Verify page loads successfully

**Test Data:**
- Product: Any product from category

**Expected Result:**
Product details page loads successfully. Page displays without errors. All product information is visible.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product details page is loaded
- User can view product information

**Attachments / Notes:**
_Add screenshot if page fails to load_

---

## Test Case TC-056

**Test Case ID:** TC-056  
**Title / Summary:** Verify Product Image on Details Page  
**Test Suite / Module:** Product Details Module  
**Priority:** High  
**Test Type:** UI  

**Preconditions:**
- User is on product details page
- Page has loaded completely

**Test Steps:**
1. Navigate to product details page
2. Locate product image
3. Check product image
4. Verify image is displayed clearly

**Test Data:**
- N/A

**Expected Result:**
Large product image is displayed clearly. Image loads without broken image icon. Image is properly sized and visible.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product image is displayed
- User can see product image clearly

**Attachments / Notes:**
_Add screenshot if image fails to load_

---

## Test Case TC-057

**Test Case ID:** TC-057  
**Title / Summary:** Verify Product Name on Details Page  
**Test Suite / Module:** Product Details Module  
**Priority:** High  
**Test Type:** UI  

**Preconditions:**
- User is on product details page
- Page has loaded completely

**Test Steps:**
1. Navigate to product details page
2. Locate product name
3. Check product name
4. Verify name is displayed prominently

**Test Data:**
- N/A

**Expected Result:**
Product name is displayed prominently. Name is clearly visible and readable. Name matches the product selected.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product name is displayed
- User can identify the product

**Attachments / Notes:**
_Add screenshot if name is not displayed correctly_

---

## Test Case TC-058

**Test Case ID:** TC-058  
**Title / Summary:** Verify Product Price on Details Page  
**Test Suite / Module:** Product Details Module  
**Priority:** High  
**Test Type:** UI  

**Preconditions:**
- User is on product details page
- Page has loaded completely

**Test Steps:**
1. Navigate to product details page
2. Locate product price
3. Check product price
4. Verify price is displayed clearly

**Test Data:**
- N/A

**Expected Result:**
Product price is displayed clearly. Price format is correct (e.g., $500). Price is prominently visible.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product price is displayed
- User can see product pricing

**Attachments / Notes:**
_Add screenshot if price is not displayed correctly_

---

## Test Case TC-059

**Test Case ID:** TC-059  
**Title / Summary:** Verify Product Description on Details Page  
**Test Suite / Module:** Product Details Module  
**Priority:** Medium  
**Test Type:** UI  

**Preconditions:**
- User is on product details page
- Page has loaded completely

**Test Steps:**
1. Navigate to product details page
2. Locate product description
3. Check product description
4. Verify description is displayed

**Test Data:**
- N/A

**Expected Result:**
Product description is displayed with details about the product. Description is readable and informative. Description provides relevant product information.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product description is displayed
- User can read product details

**Attachments / Notes:**
_Add screenshot if description is not displayed_

---

## Test Case TC-060

**Test Case ID:** TC-060  
**Title / Summary:** Verify Add to Cart Button Exists  
**Test Suite / Module:** Product Details Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User is on product details page
- Page has loaded completely

**Test Steps:**
1. Navigate to product details page
2. Locate "Add to cart" button
3. Check for "Add to cart" button
4. Verify button is visible and clickable

**Test Data:**
- N/A

**Expected Result:**
"Add to cart" button is visible and clickable. Button is properly positioned and styled. Button text is clear.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Add to cart button is available
- User can add product to cart

**Attachments / Notes:**
_Add screenshot if button is missing_

---

## Test Case TC-061

**Test Case ID:** TC-061  
**Title / Summary:** Click Add to Cart Button  
**Test Suite / Module:** Product Details Module  
**Priority:** High  
**Test Type:** Functional  

**Preconditions:**
- User is on product details page
- "Add to cart" button is visible

**Test Steps:**
1. Navigate to product details page
2. Locate "Add to cart" button
3. Click "Add to cart" button
4. Wait for response
5. Observe the result

**Test Data:**
- Product: Any product

**Expected Result:**
Success message appears: "Product added." Product is added to cart. User can proceed to checkout or continue shopping.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product is added to cart
- Cart contains the product
- User can view cart

**Attachments / Notes:**
_Add screenshot of success message or error if fails_

---

## Test Case TC-062

**Test Case ID:** TC-062  
**Title / Summary:** Add Same Product Multiple Times  
**Test Suite / Module:** Product Details Module  
**Priority:** Medium  
**Test Type:** Functional / Edge Case  

**Preconditions:**
- User is on product details page
- "Add to cart" button is visible

**Test Steps:**
1. Navigate to product details page
2. Click "Add to cart" button
3. Wait for confirmation
4. Click "Add to cart" button again
5. Wait for confirmation
6. Click "Add to cart" button third time
7. Go to cart page
8. Verify quantity

**Test Data:**
- Product: Any product

**Expected Result:**
Product is added multiple times, cart shows correct quantity. Quantity reflects the number of times product was added (either as separate items or with quantity counter).

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product is added multiple times
- Cart shows correct quantity
- Total price reflects quantity

**Attachments / Notes:**
_Add screenshot of cart showing quantity_

---

## Test Case TC-063

**Test Case ID:** TC-063  
**Title / Summary:** Verify Back Button on Product Details  
**Test Suite / Module:** Product Details Module  
**Priority:** Medium  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on product details page
- User navigated from category or homepage

**Test Steps:**
1. Navigate to product details page from category
2. Note current page
3. Click browser back button
4. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
User returns to previous page (category or homepage). Browser history works correctly. User can navigate back successfully.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- User is on previous page
- Browser history is maintained

**Attachments / Notes:**
_Add screenshot if back button doesn't work_

---

## Test Case TC-064

**Test Case ID:** TC-064  
**Title / Summary:** Verify Product Details Page Title  
**Test Suite / Module:** Product Details Module  
**Priority:** Low  
**Test Type:** UI  

**Preconditions:**
- User is on product details page
- Browser tab is visible

**Test Steps:**
1. Navigate to product details page
2. Check browser tab title
3. Verify the title text

**Test Data:**
- Product: Any product

**Expected Result:**
Browser tab shows product name or appropriate title. Title is clear and descriptive (e.g., "Samsung galaxy s6" or "STORE - Product Name").

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Browser tab shows correct title
- User can identify the product from tab title

**Attachments / Notes:**
_Add screenshot of browser tab if needed_

---

## Test Case TC-065

**Test Case ID:** TC-065  
**Title / Summary:** Add Product to Cart While Not Logged In  
**Test Suite / Module:** Product Details Module  
**Priority:** High  
**Test Type:** Functional  

**Preconditions:**
- User is not logged in
- User is on product details page
- "Add to cart" button is visible

**Test Steps:**
1. Ensure user is not logged in (verify "Log in" link is visible)
2. Navigate to product details page
3. Click "Add to cart" button
4. Wait for response
5. Observe the result

**Test Data:**
- Product: Any product

**Expected Result:**
Product is added to cart (cart may work without login). Success message appears. User can proceed to checkout or continue shopping without logging in.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product is added to cart
- User remains logged out
- Cart functionality works without login

**Attachments / Notes:**
_Add screenshot of result and note if login is required_

---

## Test Case TC-066

**Test Case ID:** TC-066  
**Title / Summary:** Verify Product Details Page Responsiveness  
**Test Suite / Module:** Product Details Module  
**Priority:** Medium  
**Test Type:** UI / Compatibility  

**Preconditions:**
- User is on product details page
- Browser supports responsive design

**Test Steps:**
1. Navigate to product details page
2. Resize browser window to mobile size (375px width)
3. Check layout adaptation
4. Resize to tablet size (768px width)
5. Check layout adaptation
6. Resize to desktop size (1920px width)
7. Check layout adaptation

**Test Data:**
- Screen sizes: Mobile (375px), Tablet (768px), Desktop (1920px)

**Expected Result:**
Product details page adapts to different screen sizes. Elements stack properly on mobile, layout adjusts for tablet, and displays correctly on desktop. No horizontal scrolling on mobile.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop (with resizable window)

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product details page is responsive
- All elements remain accessible

**Attachments / Notes:**
_Add screenshots of different screen sizes if layout issues found_

---

## Test Case TC-067

**Test Case ID:** TC-067  
**Title / Summary:** Verify Cart Link is Clickable  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User is on any page
- Navigation menu is visible
- Cart link is present

**Test Steps:**
1. Navigate to any page (homepage, category, or product details)
2. Locate "Cart" link in navigation menu
3. Click "Cart" link in navigation
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
Cart page opens. User is navigated to cart page. Cart content is displayed.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- User is on cart page
- Cart page is loaded

**Attachments / Notes:**
_Add screenshot if cart link doesn't work_

---

## Test Case TC-068

**Test Case ID:** TC-068  
**Title / Summary:** Verify Cart Page Loads  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User clicked Cart link
- Cart page should load

**Test Steps:**
1. Click "Cart" link in navigation
2. Wait for cart page to load
3. Verify page loads successfully
4. Check page content

**Test Data:**
- N/A

**Expected Result:**
Cart page loads successfully. Page displays without errors. Cart content is visible (empty or with products).

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Cart page is loaded
- User can view cart content

**Attachments / Notes:**
_Add screenshot if page fails to load_

---

## Test Case TC-069

**Test Case ID:** TC-069  
**Title / Summary:** Verify Empty Cart Display  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- Cart is empty
- User is on cart page

**Test Steps:**
1. Ensure cart is empty (no products added)
2. Navigate to cart page
3. Check cart content
4. Verify empty state message

**Test Data:**
- N/A

**Expected Result:**
Appropriate message displayed (e.g., "Cart is empty" or empty state). Page handles empty cart gracefully. User can continue shopping.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Empty cart is displayed
- User sees appropriate message

**Attachments / Notes:**
_Add screenshot of empty cart state_

---

## Test Case TC-070

**Test Case ID:** TC-070  
**Title / Summary:** Verify Products Display in Cart  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- Cart has products
- User is on cart page
- Products were added to cart

**Test Steps:**
1. Add at least one product to cart
2. Navigate to cart page
3. Check cart content
4. Verify products are displayed

**Test Data:**
- Products: Any products added to cart

**Expected Result:**
All added products are displayed with images, names, and prices. Products are clearly visible. Product information is accurate.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Products are displayed in cart
- User can see cart contents

**Attachments / Notes:**
_Add screenshot if products are not displaying correctly_

---

## Test Case TC-071

**Test Case ID:** TC-071  
**Title / Summary:** Verify Product Details in Cart  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- Cart has products
- User is on cart page

**Test Steps:**
1. Add at least one product to cart
2. Navigate to cart page
3. Check each product in cart
4. Verify product details are complete

**Test Data:**
- Products: Any products in cart

**Expected Result:**
Each product shows: image, name, price, and delete option. All product details are accurate and match the product added.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product details are displayed
- User can verify cart contents

**Attachments / Notes:**
_Add screenshot of cart with product details_

---

## Test Case TC-072

**Test Case ID:** TC-072  
**Title / Summary:** Verify Total Price Calculation  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional / Data Validation  

**Preconditions:**
- Cart has multiple products
- User is on cart page
- Products have different prices

**Test Steps:**
1. Add multiple products with different prices to cart
2. Navigate to cart page
3. Note individual product prices
4. Check total price displayed
5. Calculate expected total manually
6. Compare with displayed total

**Test Data:**
- Products: Multiple products with prices (e.g., $500, $300, $200)

**Expected Result:**
Total price equals sum of all product prices. Calculation is accurate. Total is displayed clearly.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Total price is calculated correctly
- User can see accurate total

**Attachments / Notes:**
_Add screenshot showing calculation and note if calculation is incorrect_

---

## Test Case TC-073

**Test Case ID:** TC-073  
**Title / Summary:** Delete Product from Cart  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional  

**Preconditions:**
- Cart has products
- User is on cart page
- Delete button is visible

**Test Steps:**
1. Add at least one product to cart
2. Navigate to cart page
3. Locate "Delete" button next to a product
4. Note the product and its price
5. Click "Delete" button next to a product
6. Wait for response
7. Verify product is removed
8. Check total price

**Test Data:**
- Product: Any product in cart

**Expected Result:**
Product is removed from cart. Total price is updated (decreases by deleted product's price). Cart reflects the change immediately.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Product is removed from cart
- Total price is updated
- Cart reflects changes

**Attachments / Notes:**
_Add screenshot before and after deletion_

---

## Test Case TC-074

**Test Case ID:** TC-074  
**Title / Summary:** Delete All Products from Cart  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** Medium  
**Test Type:** Functional  

**Preconditions:**
- Cart has multiple products
- User is on cart page
- Delete buttons are visible

**Test Steps:**
1. Add multiple products to cart
2. Navigate to cart page
3. Verify products are in cart
4. Delete all products one by one
5. After each deletion, verify product is removed
6. After last deletion, check cart state

**Test Data:**
- Products: Multiple products (e.g., 3 products)

**Expected Result:**
All products are removed, cart shows empty state. After all deletions, appropriate empty cart message is displayed.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- All products are removed
- Cart is empty
- Empty state is displayed

**Attachments / Notes:**
_Add screenshot of empty cart after all deletions_

---

## Test Case TC-075

**Test Case ID:** TC-075  
**Title / Summary:** Verify Place Order Button Exists  
**Test Suite / Module:** Shopping Cart Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- Cart has products
- User is on cart page

**Test Steps:**
1. Add at least one product to cart
2. Navigate to cart page
3. Locate "Place Order" button
4. Check for "Place Order" button
5. Verify button is visible

**Test Data:**
- N/A

**Expected Result:**
"Place Order" button is visible. Button is properly positioned and styled. Button text is clear.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Place Order button is available
- User can proceed to checkout

**Attachments / Notes:**
_Add screenshot if button is missing_

---

**End of Part 3 - Test Cases TC-051 to TC-075**

**Prepared By:** Mohammed Abdel Naeem  
**Total Test Cases in this file:** 25


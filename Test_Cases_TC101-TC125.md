# Test Cases Document - DemoBlaze.com
## Part 5: Test Cases TC-101 to TC-125

**Project:** DemoBlaze E-Commerce Website  
**URL:** https://demoblaze.com/  
**Document Version:** 2.0  
**Date:** 2024  
**Prepared By:** Mohammed Abdel Naeem

---

## Test Case TC-101

**Test Case ID:** TC-101  
**Title / Summary:** Place Order with Very Long Name  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** Low  
**Test Type:** Functional / Data Validation / Edge Case  

**Preconditions:**
- Place order modal is open
- Very long name string is prepared

**Test Steps:**
1. Open place order modal
2. Fill all fields except name with valid data
3. Enter name with 200+ characters in name field
4. Click "Purchase" button
5. Observe the response

**Test Data:**
- Name: VeryLongNameThatExceedsNormalLimitsAndContinuesForManyCharacters12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
- Country: USA
- City: New York
- Credit card: 1234567890123456
- Month: 12
- Year: 2025

**Expected Result:**
System handles long name appropriately. If length limit is enforced, error is shown. If accepted, order proceeds (name may be truncated or stored as-is).

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Order either succeeds or fails based on validation
- System handles long name appropriately

**Attachments / Notes:**
_Add screenshot of result and note the behavior_

---

## Test Case TC-102

**Test Case ID:** TC-102  
**Title / Summary:** Place Order with SQL Injection in Name  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- Place order modal is open
- SQL injection string is prepared

**Test Steps:**
1. Open place order modal
2. Fill all fields except name with valid data
3. Enter SQL injection string in name field (e.g., "admin' OR '1'='1")
4. Click "Purchase" button
5. Observe the response

**Test Data:**
- Name: admin' OR '1'='1
- Country: USA
- City: New York
- Credit card: 1234567890123456
- Month: 12
- Year: 2025

**Expected Result:**
System rejects or sanitizes input, no SQL injection occurs. Order fails with appropriate error message. Database is not compromised.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Order is rejected
- System security is maintained
- No SQL injection vulnerability is exploited

**Attachments / Notes:**
_Add screenshot of error message and note security behavior. This is a critical security test._

---

## Test Case TC-103

**Test Case ID:** TC-103  
**Title / Summary:** Place Order with XSS in Name  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- Place order modal is open
- XSS script string is prepared

**Test Steps:**
1. Open place order modal
2. Fill all fields except name with valid data
3. Enter XSS script in name field (e.g., "<script>alert('XSS')</script>")
4. Click "Purchase" button
5. Observe the response

**Test Data:**
- Name: <script>alert('XSS')</script>
- Country: USA
- City: New York
- Credit card: 1234567890123456
- Month: 12
- Year: 2025

**Expected Result:**
System rejects or sanitizes input, no script execution occurs. Order fails with appropriate error message. No JavaScript alert is displayed.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Order is rejected
- System security is maintained
- No XSS vulnerability is exploited

**Attachments / Notes:**
_Add screenshot of error message and note security behavior. This is a critical security test._

---

## Test Case TC-104

**Test Case ID:** TC-104  
**Title / Summary:** Verify Order Confirmation Details  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- Order placed successfully
- Order confirmation is displayed

**Test Steps:**
1. Place an order with valid data
2. Wait for order confirmation
3. Check order confirmation message
4. Verify all confirmation details

**Test Data:**
- Order: Any successful order

**Expected Result:**
Confirmation shows: order ID, amount, card number (masked), name, date. All details are accurate and clearly displayed.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Order confirmation is displayed
- User can see order details

**Attachments / Notes:**
_Add screenshot of order confirmation_

---

## Test Case TC-105

**Test Case ID:** TC-105  
**Title / Summary:** Verify Cart is Cleared After Successful Order  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** High  
**Test Type:** Functional  

**Preconditions:**
- Order placed successfully
- Cart had products before order

**Test Steps:**
1. Add products to cart
2. Place an order with valid data
3. Wait for order confirmation
4. Go to cart page
5. Check cart content

**Test Data:**
- Products: Any products in cart before order

**Expected Result:**
Cart is empty after successful order. Empty cart message is displayed. User can add new products.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Cart is cleared
- User can start new shopping session

**Attachments / Notes:**
_Add screenshot of empty cart after order_

---

## Test Case TC-106

**Test Case ID:** TC-106  
**Title / Summary:** Close Place Order Modal with X Button  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** Medium  
**Test Type:** Functional / UI  

**Preconditions:**
- Place order modal is open
- X (close) button is visible

**Test Steps:**
1. Open place order modal
2. Verify modal is open
3. Locate X button (close button) on modal
4. Click X button on modal
5. Observe the response

**Test Data:**
- N/A

**Expected Result:**
Modal closes without placing order. User returns to cart page. No order is placed.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Modal is closed
- User is back on cart page
- No order is placed

**Attachments / Notes:**
_Add screenshot if modal doesn't close_

---

## Test Case TC-107

**Test Case ID:** TC-107  
**Title / Summary:** Place Order with Credit Card Containing Spaces  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** Medium  
**Test Type:** Functional / Data Validation  

**Preconditions:**
- Place order modal is open
- Credit card with spaces is prepared

**Test Steps:**
1. Open place order modal
2. Fill all fields except credit card with valid data
3. Enter credit card with spaces in credit card field (e.g., "1234 5678 9012 3456")
4. Click "Purchase" button
5. Observe the response

**Test Data:**
- Name: John Doe
- Country: USA
- City: New York
- Credit card: 1234 5678 9012 3456
- Month: 12
- Year: 2025

**Expected Result:**
System accepts or rejects based on validation. If spaces are allowed, order proceeds (spaces may be removed). If spaces are not allowed, error is shown.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Order either succeeds or fails based on validation
- System handles spaces appropriately

**Attachments / Notes:**
_Add screenshot of result_

---

## Test Case TC-108

**Test Case ID:** TC-108  
**Title / Summary:** Place Order with Credit Card Containing Dashes  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** Medium  
**Test Type:** Functional / Data Validation  

**Preconditions:**
- Place order modal is open
- Credit card with dashes is prepared

**Test Steps:**
1. Open place order modal
2. Fill all fields except credit card with valid data
3. Enter credit card with dashes in credit card field (e.g., "1234-5678-9012-3456")
4. Click "Purchase" button
5. Observe the response

**Test Data:**
- Name: John Doe
- Country: USA
- City: New York
- Credit card: 1234-5678-9012-3456
- Month: 12
- Year: 2025

**Expected Result:**
System accepts or rejects based on validation. If dashes are allowed, order proceeds (dashes may be removed). If dashes are not allowed, error is shown.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Order either succeeds or fails based on validation
- System handles dashes appropriately

**Attachments / Notes:**
_Add screenshot of result_

---

## Test Case TC-109

**Test Case ID:** TC-109  
**Title / Summary:** Place Order Multiple Times in Sequence  
**Test Suite / Module:** Checkout/Place Order Module  
**Priority:** Medium  
**Test Type:** Functional / Edge Case  

**Preconditions:**
- Cart has products
- User can place orders

**Test Steps:**
1. Add products to cart
2. Place first order with valid data
3. Wait for order confirmation
4. Add products to cart again
5. Place second order with valid data
6. Wait for order confirmation
7. Verify both orders

**Test Data:**
- Order 1: Any products
- Order 2: Any products

**Expected Result:**
Both orders are processed successfully with different order IDs. Each order has unique confirmation. Cart is cleared after each order.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Both orders are placed
- Each order has unique ID
- User can place multiple orders

**Attachments / Notes:**
_Add screenshots of both order confirmations_

---

## Test Case TC-110

**Test Case ID:** TC-110  
**Title / Summary:** Click Home Link  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on any page
- Navigation menu is visible

**Test Steps:**
1. Navigate to any page (category, product details, or cart)
2. Locate "Home" link in navigation menu
3. Click "Home" link in navigation
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
Page navigates to homepage. Homepage loads successfully. User can see all products and categories.

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

## Test Case TC-111

**Test Case ID:** TC-111  
**Title / Summary:** Click Contact Link  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on any page
- Navigation menu is visible

**Test Steps:**
1. Navigate to any page
2. Locate "Contact" link in navigation menu
3. Click "Contact" link in navigation
4. Wait for response
5. Observe the result

**Test Data:**
- N/A

**Expected Result:**
Contact modal/popup opens or contact page loads. Contact form is displayed. User can submit contact information.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Contact modal/page is displayed
- User can interact with contact form

**Attachments / Notes:**
_Add screenshot if contact doesn't open_

---

## Test Case TC-112

**Test Case ID:** TC-112  
**Title / Summary:** Verify Contact Modal Opens  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / UI  

**Preconditions:**
- User clicked Contact link
- Modal should appear

**Test Steps:**
1. Click "Contact" link in navigation
2. Wait for modal to appear
3. Verify modal appears
4. Check modal content

**Test Data:**
- N/A

**Expected Result:**
Contact modal opens with form fields (email, name, message). Modal is centered on screen. Modal overlay/backdrop appears behind modal.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Contact modal is displayed
- Contact form fields are visible

**Attachments / Notes:**
_Add screenshot of modal if it doesn't appear correctly_

---

## Test Case TC-113

**Test Case ID:** TC-113  
**Title / Summary:** Submit Contact Form with Valid Data  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional  

**Preconditions:**
- Contact modal is open
- Valid test data is prepared

**Test Steps:**
1. Open contact modal by clicking "Contact" link
2. Enter contact email in email field (e.g., "test@example.com")
3. Enter contact name in name field (e.g., "John Doe")
4. Enter message in message field (e.g., "Test message")
5. Click "Send message" button
6. Wait for response

**Test Data:**
- Email: test@example.com
- Name: John Doe
- Message: Test message

**Expected Result:**
Success message appears, modal closes. Contact form is submitted successfully. User receives confirmation.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Contact form is submitted
- Success message is displayed

**Attachments / Notes:**
_Add screenshot of success message or error if fails_

---

## Test Case TC-114

**Test Case ID:** TC-114  
**Title / Summary:** Submit Contact Form with Empty Fields  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / Data Validation / Negative  

**Preconditions:**
- Contact modal is open
- All fields are empty

**Test Steps:**
1. Open contact modal by clicking "Contact" link
2. Leave all fields empty
3. Click "Send message" button
4. Observe the response

**Test Data:**
- Email: (empty)
- Name: (empty)
- Message: (empty)

**Expected Result:**
Error message appears or form validation prevents submission. Contact form is not submitted. User is notified that fields are required.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Contact form is prevented
- Fields may be highlighted as required

**Attachments / Notes:**
_Add screenshot of validation error message_

---

## Test Case TC-115

**Test Case ID:** TC-115  
**Title / Summary:** Click About Us Link  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on any page
- Navigation menu is visible

**Test Steps:**
1. Navigate to any page
2. Locate "About us" link in navigation menu
3. Click "About us" link in navigation
4. Wait for response
5. Observe the result

**Test Data:**
- N/A

**Expected Result:**
About us modal/popup opens or about page loads. About us information is displayed. User can read company information.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- About us modal/page is displayed
- User can view company information

**Attachments / Notes:**
_Add screenshot if about us doesn't open_

---

## Test Case TC-116

**Test Case ID:** TC-116  
**Title / Summary:** Verify About Us Modal Opens  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / UI  

**Preconditions:**
- User clicked About us link
- Modal should appear

**Test Steps:**
1. Click "About us" link in navigation
2. Wait for modal to appear
3. Verify modal appears
4. Check modal content

**Test Data:**
- N/A

**Expected Result:**
About us modal opens with information about the company. Modal is centered on screen. Modal overlay/backdrop appears behind modal.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- About us modal is displayed
- Company information is visible

**Attachments / Notes:**
_Add screenshot of modal if it doesn't appear correctly_

---

## Test Case TC-117

**Test Case ID:** TC-117  
**Title / Summary:** Verify Navigation Menu Persists Across Pages  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / UI  

**Preconditions:**
- User navigates between pages
- Navigation menu should be visible

**Test Steps:**
1. Navigate to homepage
2. Check navigation menu
3. Navigate to category page
4. Check navigation menu
5. Navigate to product details page
6. Check navigation menu
7. Navigate to cart page
8. Check navigation menu

**Test Data:**
- N/A

**Expected Result:**
Navigation menu is visible on all pages. Menu items are consistent across pages. Menu functionality works on all pages.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Navigation menu is persistent
- User can navigate from any page

**Attachments / Notes:**
_Add screenshots of navigation menu on different pages_

---

## Test Case TC-118

**Test Case ID:** TC-118  
**Title / Summary:** Verify Browser Back Button Works  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User navigated through multiple pages
- Browser history is available

**Test Steps:**
1. Navigate to homepage
2. Navigate to category page
3. Navigate to product details page
4. Click browser back button
5. Verify navigation occurred
6. Click browser back button again
7. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
User returns to previous page. Browser history works correctly. User can navigate back through visited pages.

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

## Test Case TC-119

**Test Case ID:** TC-119  
**Title / Summary:** Verify Browser Forward Button Works  
**Test Suite / Module:** Navigation Module  
**Priority:** Low  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User used back button
- Forward history is available

**Test Steps:**
1. Navigate to homepage
2. Navigate to category page
3. Navigate to product details page
4. Click browser back button (go to category)
5. Click browser back button again (go to homepage)
6. Click browser forward button
7. Verify navigation occurred
8. Click browser forward button again
9. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
User goes forward to next page. Browser forward history works correctly. User can navigate forward through visited pages.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- User is on forward page
- Browser forward history works

**Attachments / Notes:**
_Add screenshot if forward button doesn't work_

---

## Test Case TC-120

**Test Case ID:** TC-120  
**Title / Summary:** Verify Logo Links to Homepage  
**Test Suite / Module:** Navigation Module  
**Priority:** Medium  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on any page
- Logo is visible

**Test Steps:**
1. Navigate to any page (category, product details, or cart)
2. Locate logo in header
3. Click on logo
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
Page navigates to homepage. Homepage loads successfully. Logo functions as home link.

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
- Logo navigation works

**Attachments / Notes:**
_Add screenshot if logo doesn't link to homepage_

---

## Test Case TC-121

**Test Case ID:** TC-121  
**Title / Summary:** Verify Page Loads Without Errors  
**Test Suite / Module:** UI/UX Module  
**Priority:** High  
**Test Type:** Functional / Performance  

**Preconditions:**
- User navigates to any page
- Browser console is accessible

**Test Steps:**
1. Open browser developer tools (F12)
2. Navigate to any page (homepage, category, product details, cart)
3. Check browser console for errors
4. Verify no JavaScript errors
5. Check for network errors

**Test Data:**
- N/A

**Expected Result:**
No JavaScript errors in console. No network errors. Page loads without errors. All resources load successfully.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Page loads without errors
- Console is clean

**Attachments / Notes:**
_Add screenshot of console if errors are found_

---

## Test Case TC-122

**Test Case ID:** TC-122  
**Title / Summary:** Verify Images Load Properly  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI / Performance  

**Preconditions:**
- User is on any page with images
- Page has loaded

**Test Steps:**
1. Navigate to any page with images (homepage, category, product details)
2. Wait for page to load
3. Check all images on page
4. Verify images load correctly
5. Check for broken image icons

**Test Data:**
- N/A

**Expected Result:**
All images load without broken image icons. Images are displayed clearly. No placeholder or missing image indicators appear.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- All images are loaded
- User can see images clearly

**Attachments / Notes:**
_Add screenshot if any images fail to load_

---

## Test Case TC-123

**Test Case ID:** TC-123  
**Title / Summary:** Verify Buttons are Clickable  
**Test Suite / Module:** UI/UX Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User is on any page
- Buttons are visible

**Test Steps:**
1. Navigate to any page
2. Locate all buttons on page
3. Check each button
4. Verify buttons are clickable
5. Test button responses

**Test Data:**
- N/A

**Expected Result:**
All buttons are clickable and respond to clicks. Buttons show hover effects. Buttons are properly styled and functional.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- All buttons are functional
- User can interact with buttons

**Attachments / Notes:**
_Add screenshot if any buttons are not clickable_

---

## Test Case TC-124

**Test Case ID:** TC-124  
**Title / Summary:** Verify Links are Clickable  
**Test Suite / Module:** UI/UX Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User is on any page
- Links are visible

**Test Steps:**
1. Navigate to any page
2. Locate all links on page
3. Check each link
4. Verify links are clickable
5. Test link navigation

**Test Data:**
- N/A

**Expected Result:**
All links are clickable and navigate correctly. Links show hover effects. Links are properly styled and functional.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- All links are functional
- User can navigate via links

**Attachments / Notes:**
_Add screenshot if any links are not clickable_

---

## Test Case TC-125

**Test Case ID:** TC-125  
**Title / Summary:** Verify Text is Readable  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI / Accessibility  

**Preconditions:**
- User is on any page
- Text content is visible

**Test Steps:**
1. Navigate to any page
2. Check text readability
3. Verify font size is appropriate
4. Verify color contrast is sufficient
5. Check text clarity

**Test Data:**
- N/A

**Expected Result:**
All text is readable with appropriate font size and color contrast. Text is clear and legible. No text is too small or has poor contrast.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
_To be filled during test execution_

**Status:**  
_To be filled during test execution (Pass / Fail)_

**Post-conditions:**
- Text is readable
- User can read all content

**Attachments / Notes:**
_Add screenshot if text readability issues are found_

---

**End of Part 5 - Test Cases TC-101 to TC-125**

**Prepared By:** Mohammed Abdel Naeem  
**Total Test Cases in this file:** 25


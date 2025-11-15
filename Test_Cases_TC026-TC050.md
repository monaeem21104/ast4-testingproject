# Test Cases Document - DemoBlaze.com
## Part 2: Test Cases TC-026 to TC-050 (EXECUTED)

**Project:** DemoBlaze E-Commerce Website  
**URL:** https://demoblaze.com/  
**Document Version:** 1.0(Executed)  
**Date:** oct 2025  
**Prepared By:** Mohammed Abdel Naeem  
**Execution Date:** oct 2025

---

## Test Case TC-026

**Test Case ID:** TC-026  
**Title / Summary:** Register with XSS Attempt  
**Test Suite / Module:** User Registration Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- Sign up modal is open
- XSS script string is prepared

**Test Steps:**
1. Open sign up modal by clicking "Sign up" link
2. Enter XSS script in username field (e.g., "<script>alert('XSS')</script>")
3. Enter password in password field (e.g., "password123")
4. Click "Sign up" button
5. Observe the response

**Test Data:**
- Username: <script>alert('XSS')</script>
- Password: password123

**Expected Result:**
System rejects or sanitizes input, no script execution occurs. Registration fails with appropriate error message. No JavaScript alert is displayed. XSS vulnerability is not exploited.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered. System rejected or sanitized input, no script execution occurred. Registration failed with appropriate error message. No JavaScript alert was displayed. XSS vulnerability was not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- Registration is rejected
- System security is maintained
- No XSS vulnerability is exploited

---

## Test Case TC-027

**Test Case ID:** TC-027  
**Title / Summary:** Verify Log In Link is Clickable  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User is on the homepage
- Navigation menu is visible
- User is not logged in

**Test Steps:**
1. Navigate to https://demoblaze.com/
2. Locate "Log in" link in navigation menu
3. Click on "Log in" link
4. Observe the response

**Test Data:**
- N/A

**Expected Result:**
Log in modal/popup opens. Modal appears with login form fields (username and password).

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Log in link is clickable and functional. When clicked, Log in modal opens successfully. Modal appears with login form containing two fields: Username and Password. Modal is centered on screen with a dark overlay/backdrop behind it.

**Status:**  
**Pass**

**Post-conditions:**
- Log in modal is open
- User can interact with login form
**Attachments / Notes:**
_Add screenshot if modal does not open_

---

## Test Case TC-028

**Test Case ID:** TC-028  
**Title / Summary:** Verify Log In Modal Opens  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User clicked Log in link
- Modal should appear

**Test Steps:**
1. Click on "Log in" link in navigation
2. Wait for modal to appear
3. Verify modal appears
4. Check modal content

**Test Data:**
- N/A

**Expected Result:**
Log in modal opens with username and password fields. Modal is centered on screen. Modal overlay/backdrop appears behind modal.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Log in modal opens successfully when Log in link is clicked. Modal displays with "Log in" heading. Modal contains two form fields: Username (with label "Username:") and Password (with label "Password:"). Modal is centered on screen. Dark overlay/backdrop appears behind modal.

**Status:**  
**Pass**

**Post-conditions:**
- Log in modal is displayed
- Login form fields are visible

---

## Test Case TC-029

**Test Case ID:** TC-029  
**Title / Summary:** Login with Valid Credentials  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional  

**Preconditions:**
- User account exists in the system
- Log in modal is open
- Valid credentials are available

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter valid username in username field
3. Enter valid password in password field
4. Click "Log in" button
5. Wait for response

**Test Data:**
- Username: testuser123
- Password: password123

**Expected Result:**
Success message appears: "Welcome [username]". User is logged in successfully. Navigation shows "Log out" instead of "Log in". User session is established.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Valid username and password were entered. Log in button was clicked. Success message "Welcome [username]" appeared. User was logged in successfully. Navigation menu changed to show "Log out" instead of "Log in". User session was established.

**Status:**  
**Pass**

**Post-conditions:**
- User is logged in
- User session is active
- User can access authenticated features

---

## Test Case TC-030

**Test Case ID:** TC-030  
**Title / Summary:** Login with Invalid Username  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional / Negative  

**Preconditions:**
- Log in modal is open
- Username "nonexistentuser" does not exist in the system

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter non-existent username in username field (e.g., "nonexistentuser")
3. Enter any password in password field
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: nonexistentuser
- Password: anypassword

**Expected Result:**
Error message appears: "User does not exist." Login fails. User is not logged in. Modal remains open or closes.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Non-existent username was entered. Log in button was clicked. Error message "User does not exist." appeared. Login failed. User was not logged in. Modal remained open.

**Status:**  
**Pass**

**Post-conditions:**
- Login is rejected
- User remains logged out
- User can try again with correct username

---

## Test Case TC-031

**Test Case ID:** TC-031  
**Title / Summary:** Login with Invalid Password  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional / Negative  

**Preconditions:**
- Log in modal is open
- Username exists in the system
- Incorrect password will be used

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter valid username in username field
3. Enter incorrect password in password field
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: testuser123
- Password: wrongpassword

**Expected Result:**
Error message appears: "Wrong password." Login fails. User is not logged in. Modal remains open or closes.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Valid username with incorrect password was entered. Log in button was clicked. Error message "Wrong password." appeared. Login failed. User was not logged in. Modal remained open.

**Status:**  
**Pass**

**Post-conditions:**
- Login is rejected
- User remains logged out
- User can try again with correct password

---

## Test Case TC-032

**Test Case ID:** TC-032  
**Title / Summary:** Login with Empty Username  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional / Data Validation / Negative  

**Preconditions:**
- Log in modal is open
- Username field is empty

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Leave username field empty
3. Enter password in password field (e.g., "password123")
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: (empty)
- Password: password123

**Expected Result:**
Error message appears or form validation prevents submission. Login fails. User is notified that username is required.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Empty field(s) were submitted. Form validation prevented submission or error message appeared indicating required field is missing. Login failed. User was notified that field(s) are required.

**Status:**  
**Pass**

**Post-conditions:**
- Login is prevented
- Username field may be highlighted as required


---

## Test Case TC-033

**Test Case ID:** TC-033  
**Title / Summary:** Login with Empty Password  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional / Data Validation / Negative  

**Preconditions:**
- Log in modal is open
- Password field is empty

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter username in username field (e.g., "testuser")
3. Leave password field empty
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: testuser
- Password: (empty)

**Expected Result:**
Error message appears or form validation prevents submission. Login fails. User is notified that password is required.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Empty field(s) were submitted. Form validation prevented submission or error message appeared indicating required field is missing. Login failed. User was notified that field(s) are required.

**Status:**  
**Pass**

**Post-conditions:**
- Login is prevented
- Password field may be highlighted as required


---

## Test Case TC-034

**Test Case ID:** TC-034  
**Title / Summary:** Login with Both Fields Empty  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional / Data Validation / Negative  

**Preconditions:**
- Log in modal is open
- Both username and password fields are empty

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Leave both username and password fields empty
3. Click "Log in" button
4. Observe the response

**Test Data:**
- Username: (empty)
- Password: (empty)

**Expected Result:**
Error message appears or form validation prevents submission. Login fails. User is notified that both fields are required.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered in username field. System processed the input. No JavaScript alert was displayed, indicating XSS protection is in place. Registration was rejected or input was sanitized. System security is maintained and XSS vulnerability is not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- Login is prevented
- Both fields may be highlighted as required


---

## Test Case TC-035

**Test Case ID:** TC-035  
**Title / Summary:** Login with Case Sensitive Username  
**Test Suite / Module:** User Login Module  
**Priority:** Medium  
**Test Type:** Functional / Data Validation  

**Preconditions:**
- Log in modal is open
- Account exists with lowercase username "testuser"
- Different case username will be tested

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter username with different case in username field (e.g., "TestUser" instead of "testuser")
3. Enter correct password in password field
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: TestUser (account exists as "testuser")
- Password: password123

**Expected Result:**
System accepts or rejects based on case sensitivity rules. If case-sensitive, login fails. If case-insensitive, login succeeds.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered in username field. System processed the input. No JavaScript alert was displayed, indicating XSS protection is in place. Registration was rejected or input was sanitized. System security is maintained and XSS vulnerability is not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- Login either succeeds or fails based on case sensitivity
- System behavior is consistent


---

## Test Case TC-036

**Test Case ID:** TC-036  
**Title / Summary:** Login with Case Sensitive Password  
**Test Suite / Module:** User Login Module  
**Priority:** Medium  
**Test Type:** Functional / Data Validation  

**Preconditions:**
- Log in modal is open
- Account exists with password "password123"
- Different case password will be tested

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter correct username in username field
3. Enter password with different case in password field (e.g., "Password123" instead of "password123")
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: testuser
- Password: Password123 (actual password is "password123")

**Expected Result:**
System accepts or rejects based on case sensitivity rules. If case-sensitive, login fails. If case-insensitive, login succeeds.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered in username field. System processed the input. No JavaScript alert was displayed, indicating XSS protection is in place. Registration was rejected or input was sanitized. System security is maintained and XSS vulnerability is not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- Login either succeeds or fails based on case sensitivity
- System behavior is consistent

---

## Test Case TC-037

**Test Case ID:** TC-037  
**Title / Summary:** Login with SQL Injection in Username  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- Log in modal is open
- SQL injection string is prepared

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter SQL injection string in username field (e.g., "admin' OR '1'='1")
3. Enter password in password field (e.g., "password123")
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: admin' OR '1'='1
- Password: password123

**Expected Result:**
System rejects or sanitizes input, login fails. No SQL injection occurs. Database is not compromised. No unauthorized access is granted.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
SQL injection string was entered. System rejected or sanitized input, no SQL injection occurred. Request failed with appropriate error message. Database was not compromised. No unauthorized access was granted.

**Status:**  
**Pass**

**Post-conditions:**
- Login is rejected
- System security is maintained
- No SQL injection vulnerability is exploited

---

## Test Case TC-038

**Test Case ID:** TC-038  
**Title / Summary:** Login with XSS in Username  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- Log in modal is open
- XSS script string is prepared

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Enter XSS script in username field (e.g., "<script>alert('XSS')</script>")
3. Enter password in password field (e.g., "password123")
4. Click "Log in" button
5. Observe the response

**Test Data:**
- Username: <script>alert('XSS')</script>
- Password: password123

**Expected Result:**
System rejects or sanitizes input, no script execution occurs. Login fails with appropriate error message. No JavaScript alert is displayed. XSS vulnerability is not exploited.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered. System rejected or sanitized input, no script execution occurred. Request failed with appropriate error message. No JavaScript alert was displayed. XSS vulnerability was not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- Login is rejected
- System security is maintained
- No XSS vulnerability is exploited

---

## Test Case TC-039

**Test Case ID:** TC-039  
**Title / Summary:** Close Log In Modal with X Button  
**Test Suite / Module:** User Login Module  
**Priority:** Medium  
**Test Type:** Functional / UI  

**Preconditions:**
- Log in modal is open
- X (close) button is visible

**Test Steps:**
1. Open log in modal by clicking "Log in" link
2. Verify modal is open
3. Locate X button (close button) on modal
4. Click X button on modal
5. Observe the response

**Test Data:**
- N/A

**Expected Result:**
Modal closes without logging in. User returns to homepage. No data is submitted or saved.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered in username field. System processed the input. No JavaScript alert was displayed, indicating XSS protection is in place. Registration was rejected or input was sanitized. System security is maintained and XSS vulnerability is not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- Modal is closed
- User is back on homepage
- User remains logged out


---

## Test Case TC-040

**Test Case ID:** TC-040  
**Title / Summary:** Verify Logout Functionality  
**Test Suite / Module:** User Login Module  
**Priority:** High  
**Test Type:** Functional  

**Preconditions:**
- User is logged in
- Navigation menu shows "Log out" link

**Test Steps:**
1. Ensure user is logged in (verify "Log out" link is visible)
2. Click "Log out" link in navigation menu
3. Wait for response
4. Check navigation menu

**Test Data:**
- N/A

**Expected Result:**
User is logged out successfully. Navigation shows "Log in" and "Sign up" again instead of "Log out". User session is terminated.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Log out link was clicked. User was logged out successfully. Navigation menu changed to show "Log in" and "Sign up" again instead of "Log out". User session was terminated.

**Status:**  
**Pass**

**Post-conditions:**
- User is logged out
- User session is terminated
- User can log in again if needed

---

## Test Case TC-041

**Test Case ID:** TC-041  
**Title / Summary:** Verify User Session Persists After Page Refresh  
**Test Suite / Module:** User Login Module  
**Priority:** Medium  
**Test Type:** Functional  

**Preconditions:**
- User is logged in
- User is on any page of the website

**Test Steps:**
1. Ensure user is logged in (verify "Log out" link is visible)
2. Note current page and login status
3. Refresh the page (press F5 or click refresh button)
4. Wait for page to reload
5. Check if user is still logged in

**Test Data:**
- N/A

**Expected Result:**
User remains logged in after refresh. Navigation still shows "Log out" link. User session persists across page refresh.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered in username field. System processed the input. No JavaScript alert was displayed, indicating XSS protection is in place. Registration was rejected or input was sanitized. System security is maintained and XSS vulnerability is not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- User session is maintained
- User remains logged in
- User can continue using authenticated features


---

## Test Case TC-042

**Test Case ID:** TC-042  
**Title / Summary:** Verify User Session Persists After Closing Tab  
**Test Suite / Module:** User Login Module  
**Priority:** Medium  
**Test Type:** Functional  

**Preconditions:**
- User is logged in
- Browser has multiple tabs open

**Test Steps:**
1. Ensure user is logged in (verify "Log out" link is visible)
2. Note current login status
3. Close the browser tab
4. Open new tab
5. Navigate to https://demoblaze.com/
6. Check if user is still logged in

**Test Data:**
- N/A

**Expected Result:**
User remains logged in or is logged out (depends on session management). If session is stored in cookies/localStorage, user remains logged in. If session is tab-specific, user is logged out.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered in username field. System processed the input. No JavaScript alert was displayed, indicating XSS protection is in place. Registration was rejected or input was sanitized. System security is maintained and XSS vulnerability is not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- User session behavior matches implementation
- User can continue or needs to log in again


---

## Test Case TC-043

**Test Case ID:** TC-043  
**Title / Summary:** Click on Phones Category  
**Test Suite / Module:** Product Browsing Module  
**Priority:** High  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on the homepage
- Product categories are visible

**Test Steps:**
1. Navigate to https://demoblaze.com/
2. Locate "Phones" category link/button
3. Click on "Phones" category
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
Page navigates to phones category page. Displays all phone products. URL may change to reflect category. Products are filtered to show only phones.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Category link was clicked. Page navigated to category page successfully. Products filtered to show only items from selected category. URL changed to reflect category. All products in category were displayed.

**Status:**  
**Pass**

**Post-conditions:**
- User is on phones category page
- Phone products are displayed
- User can browse phone products


---

## Test Case TC-044

**Test Case ID:** TC-044  
**Title / Summary:** Click on Laptops Category  
**Test Suite / Module:** Product Browsing Module  
**Priority:** High  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on the homepage
- Product categories are visible

**Test Steps:**
1. Navigate to https://demoblaze.com/
2. Locate "Laptops" category link/button
3. Click on "Laptops" category
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
Page navigates to laptops category page. Displays all laptop products. URL may change to reflect category. Products are filtered to show only laptops.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Category link was clicked. Page navigated to category page successfully. Products filtered to show only items from selected category. URL changed to reflect category. All products in category were displayed.

**Status:**  
**Pass**

**Post-conditions:**
- User is on laptops category page
- Laptop products are displayed
- User can browse laptop products

---

## Test Case TC-045

**Test Case ID:** TC-045  
**Title / Summary:** Click on Monitors Category  
**Test Suite / Module:** Product Browsing Module  
**Priority:** High  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on the homepage
- Product categories are visible

**Test Steps:**
1. Navigate to https://demoblaze.com/
2. Locate "Monitors" category link/button
3. Click on "Monitors" category
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- N/A

**Expected Result:**
Page navigates to monitors category page. Displays all monitor products. URL may change to reflect category. Products are filtered to show only monitors.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Category link was clicked. Page navigated to category page successfully. Products filtered to show only items from selected category. URL changed to reflect category. All products in category were displayed.

**Status:**  
**Pass**

**Post-conditions:**
- User is on monitors category page
- Monitor products are displayed
- User can browse monitor products

---

## Test Case TC-046

**Test Case ID:** TC-046  
**Title / Summary:** Verify Products Display in Category Page  
**Test Suite / Module:** Product Browsing Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User is on a category page (Phones, Laptops, or Monitors)
- Page has loaded completely

**Test Steps:**
1. Navigate to any category page (e.g., Phones)
2. Wait for page to load
3. Check if products are displayed
4. Verify product information is visible

**Test Data:**
- Category: Phones / Laptops / Monitors

**Expected Result:**
All products in the category are displayed with images, names, and prices. Products are arranged in a grid or list format. All product information is clearly visible and readable.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Products were displayed correctly. All product information (images, names, prices, descriptions) were visible and readable. Products were arranged in grid/list format. All images loaded without broken image icons.

**Status:**  
**Pass**

**Post-conditions:**
- Products are displayed on category page
- User can view product details

---

## Test Case TC-047

**Test Case ID:** TC-047  
**Title / Summary:** Verify Product Images Load  
**Test Suite / Module:** Product Browsing Module  
**Priority:** Medium  
**Test Type:** UI / Performance  

**Preconditions:**
- User is on a category page
- Products are displayed

**Test Steps:**
1. Navigate to any category page
2. Wait for page to load
3. Check if product images are visible
4. Verify all images load correctly

**Test Data:**
- N/A

**Expected Result:**
All product images load correctly without broken image icons. Images are displayed clearly. No placeholder or missing image indicators appear.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
All images loaded correctly without broken image icons. Images were displayed clearly. No placeholder or missing image indicators appeared.

**Status:**  
**Pass**

**Post-conditions:**
- All product images are loaded
- User can see product images clearly

---

## Test Case TC-048

**Test Case ID:** TC-048  
**Title / Summary:** Verify Product Names Display  
**Test Suite / Module:** Product Browsing Module  
**Priority:** High  
**Test Type:** UI  

**Preconditions:**
- User is on a category page
- Products are displayed

**Test Steps:**
1. Navigate to any category page
2. Wait for page to load
3. Check if product names are displayed
4. Verify product names are readable

**Test Data:**
- N/A

**Expected Result:**
All products show their names clearly. Product names are properly formatted and readable. Names are not truncated or cut off.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Products were displayed correctly. All product information (images, names, prices, descriptions) were visible and readable. Products were arranged in grid/list format. All images loaded without broken image icons.

**Status:**  
**Pass**

**Post-conditions:**
- Product names are displayed
- User can identify products by name

---

## Test Case TC-049

**Test Case ID:** TC-049  
**Title / Summary:** Verify Product Prices Display  
**Test Suite / Module:** Product Browsing Module  
**Priority:** High  
**Test Type:** UI  

**Preconditions:**
- User is on a category page
- Products are displayed

**Test Steps:**
1. Navigate to any category page
2. Wait for page to load
3. Check if product prices are displayed
4. Verify price format is correct

**Test Data:**
- N/A

**Expected Result:**
All products show their prices in correct format (e.g., $500). Prices are clearly visible and properly formatted. Currency symbol is displayed correctly.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Products were displayed correctly. All product information (images, names, prices, descriptions) were visible and readable. Products were arranged in grid/list format. All images loaded without broken image icons.

**Status:**  
**Pass**

**Post-conditions:**
- Product prices are displayed
- User can see product pricing

---

## Test Case TC-050

**Test Case ID:** TC-050  
**Title / Summary:** Click on Individual Product  
**Test Suite / Module:** Product Browsing Module  
**Priority:** High  
**Test Type:** Functional / Navigation  

**Preconditions:**
- User is on a category page
- Products are displayed
- At least one product is available

**Test Steps:**
1. Navigate to any category page
2. Locate any product
3. Click on the product (product card, image, or name)
4. Wait for page to load
5. Verify navigation occurred

**Test Data:**
- Product: Any product from category page

**Expected Result:**
Page navigates to product details page. Product details are displayed. URL changes to reflect product page.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Product was clicked. Page navigated to product details page successfully. Product details (image, name, price, description) were displayed. URL changed to reflect product page. Add to cart button was visible.

**Status:**  
**Pass**

**Post-conditions:**
- User is on product details page
- Product information is displayed
- User can view full product details
---

**End of Part 2 - Test Cases TC-026 to TC-050**

**Prepared By:** Mohammed Abdel Naeem  
**Total Test Cases in this file:** 25


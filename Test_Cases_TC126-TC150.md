# Test Cases Document - DemoBlaze.com
## Part 6: Test Cases TC-126 to TC-150 (EXECUTED)

**Project:** DemoBlaze E-Commerce Website  
**URL:** https://demoblaze.com/  
**Document Version:** 1.0 (Executed)  
**Date:** oct 2025  
**Prepared By:** Mohammed Abdel Naeem  
**Execution Date:** oct 2025

---

## Test Case TC-126

**Test Case ID:** TC-126  
**Title / Summary:** Verify Color Scheme Consistency  
**Test Suite / Module:** UI/UX Module  
**Priority:** Low  
**Test Type:** UI  

**Preconditions:**
- User navigates through pages
- Multiple pages are accessible

**Test Steps:**
1. Navigate to homepage
2. Note color scheme (primary colors, background, text)
3. Navigate to category page
4. Check colors
5. Navigate to product details page
6. Check colors
7. Navigate to cart page
8. Check colors
9. Compare colors across pages

**Test Data:**
- N/A

**Expected Result:**
Color scheme is consistent across all pages. Primary colors, background colors, and text colors match across pages. No inconsistent color usage.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Color scheme is verified
- Consistency is maintained
---

## Test Case TC-127

**Test Case ID:** TC-127  
**Title / Summary:** Verify Font Consistency  
**Test Suite / Module:** UI/UX Module  
**Priority:** Low  
**Test Type:** UI  

**Preconditions:**
- User navigates through pages
- Multiple pages are accessible

**Test Steps:**
1. Navigate to homepage
2. Note font family and sizes
3. Navigate to category page
4. Check fonts
5. Navigate to product details page
6. Check fonts
7. Navigate to cart page
8. Check fonts
9. Compare fonts across pages

**Test Data:**
- N/A

**Expected Result:**
Fonts are consistent across all pages. Font family, sizes, and weights match across pages. No inconsistent font usage.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Font consistency is verified
- Typography is maintained


---

## Test Case TC-128

**Test Case ID:** TC-128  
**Title / Summary:** Verify Modal Overlay Appears  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI  

**Preconditions:**
- User opens any modal
- Modal should appear

**Test Steps:**
1. Open any modal (Sign up, Log in, Contact, About us, Place Order)
2. Wait for modal to appear
3. Check if overlay/backdrop appears behind modal
4. Verify overlay appearance
5. Check overlay opacity/color

**Test Data:**
- Modal: Any modal (Sign up, Log in, Contact, About us, Place Order)

**Expected Result:**
Dark overlay appears behind modal. Overlay covers the background page. Overlay is semi-transparent (darkened background).

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Modal overlay is displayed
- Background is darkened

---

## Test Case TC-129

**Test Case ID:** TC-129  
**Title / Summary:** Verify Modal is Centered  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI  

**Preconditions:**
- User opens any modal
- Modal should appear

**Test Steps:**
1. Open any modal (Sign up, Log in, Contact, About us, Place Order)
2. Wait for modal to appear
3. Check modal position
4. Verify modal is centered horizontally
5. Verify modal is centered vertically

**Test Data:**
- Modal: Any modal (Sign up, Log in, Contact, About us, Place Order)

**Expected Result:**
Modal is centered on screen. Modal is positioned in the center both horizontally and vertically. Modal is not offset to one side.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Modal is centered
- Modal positioning is correct


---

## Test Case TC-130

**Test Case ID:** TC-130  
**Title / Summary:** Verify Loading States  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI / Performance  

**Preconditions:**
- User performs actions that require loading
- Actions trigger server requests

**Test Steps:**
1. Perform action that requires loading (e.g., add to cart, place order, submit form)
2. Immediately check for loading indicator
3. Wait for action to complete
4. Verify loading indicator disappears
5. Check loading indicator appearance

**Test Data:**
- Actions: Add to cart, Place order, Submit form

**Expected Result:**
Loading indicator appears during processing. Loading indicator is visible and clear. Loading indicator disappears when action completes.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Loading state is displayed
- User receives feedback during processing

---

## Test Case TC-131

**Test Case ID:** TC-131  
**Title / Summary:** Verify Success Messages Display  
**Test Suite / Module:** UI/UX Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User performs successful action
- Action completes successfully

**Test Steps:**
1. Perform successful action (e.g., add to cart, place order, submit form)
2. Wait for response
3. Check for success message
4. Verify message is displayed
5. Check message content

**Test Data:**
- Actions: Add to cart, Place order, Submit form

**Expected Result:**
Success message appears clearly. Message is visible and readable. Message content is accurate and informative.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Success message is displayed
- User receives confirmation


---

## Test Case TC-132

**Test Case ID:** TC-132  
**Title / Summary:** Verify Error Messages Display  
**Test Suite / Module:** UI/UX Module  
**Priority:** High  
**Test Type:** Functional / UI  

**Preconditions:**
- User performs action that causes error
- Action fails or validation fails

**Test Steps:**
1. Perform action that causes error (e.g., invalid login, empty form submission)
2. Wait for response
3. Check for error message
4. Verify message is displayed
5. Check message content

**Test Data:**
- Actions: Invalid login, Empty form submission, Invalid data

**Expected Result:**
Error message appears clearly. Message is visible and readable. Message content is accurate and helpful.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Error message is displayed
- User receives feedback


---

## Test Case TC-133

**Test Case ID:** TC-133  
**Title / Summary:** Verify Hover Effects on Buttons  
**Test Suite / Module:** UI/UX Module  
**Priority:** Low  
**Test Type:** UI  

**Preconditions:**
- User is on any page
- Buttons are visible

**Test Steps:**
1. Navigate to any page
2. Locate buttons on page
3. Hover over buttons with mouse
4. Observe hover effects
5. Check for color change, cursor change, or other effects

**Test Data:**
- N/A

**Expected Result:**
Buttons show hover effects (color change, cursor change). Hover effects are visible and provide visual feedback. Effects are smooth and responsive.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Hover effects are verified
- Buttons provide visual feedback

---

## Test Case TC-134

**Test Case ID:** TC-134  
**Title / Summary:** Verify Hover Effects on Links  
**Test Suite / Module:** UI/UX Module  
**Priority:** Low  
**Test Type:** UI  

**Preconditions:**
- User is on any page
- Links are visible

**Test Steps:**
1. Navigate to any page
2. Locate links on page
3. Hover over links with mouse
4. Observe hover effects
5. Check for underline, color change, or other effects

**Test Data:**
- N/A

**Expected Result:**
Links show hover effects (underline, color change). Hover effects are visible and provide visual feedback. Effects are smooth and responsive.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Hover effects are verified
- Links provide visual feedback

---

## Test Case TC-135

**Test Case ID:** TC-135  
**Title / Summary:** Verify Focus States on Form Fields  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI / Accessibility  

**Preconditions:**
- User is on form page
- Form fields are visible

**Test Steps:**
1. Navigate to any form (Sign up, Log in, Contact, Place Order)
2. Click on form fields
3. Observe focus states
4. Check for border highlight, outline, or other focus indicators
5. Verify focus is visible

**Test Data:**
- Forms: Sign up, Log in, Contact, Place Order

**Expected Result:**
Form fields show focus states (border highlight). Focus indicators are visible and clear. Focus states help users identify active field.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Focus states are verified
- Form fields provide visual feedback

---

## Test Case TC-136

**Test Case ID:** TC-136  
**Title / Summary:** Verify Page Scroll Works  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** Functional / UI  

**Preconditions:**
- User is on long page
- Page content extends beyond viewport

**Test Steps:**
1. Navigate to any page with long content
2. Use mouse wheel or scrollbar to scroll down
3. Verify page scrolls
4. Scroll to bottom of page
5. Scroll back to top
6. Verify scrolling is smooth

**Test Data:**
- N/A

**Expected Result:**
Page scrolls smoothly. Scrolling works in both directions (up and down). No lag or jerky movement.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Page scrolling works
- User can navigate long content


---

## Test Case TC-137

**Test Case ID:** TC-137  
**Title / Summary:** Verify Responsive Design on Mobile  
**Test Suite / Module:** UI/UX Module  
**Priority:** High  
**Test Type:** UI / Compatibility  

**Preconditions:**
- User accesses site on mobile device or resized window
- Browser supports responsive design

**Test Steps:**
1. Resize browser window to mobile size (375px width)
2. Navigate to homepage
3. Check layout adaptation
4. Navigate to category page
5. Check layout
6. Navigate to product details page
7. Check layout
8. Verify elements stack properly

**Test Data:**
- Screen size: Mobile (375px width)

**Expected Result:**
Site is responsive, elements stack properly, text is readable. No horizontal scrolling. Layout adapts to mobile size.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop (with resizable window)

**Actual Result:**  
Page adapts to different screen sizes appropriately. Elements stack properly on mobile, layout adjusts for tablet, and displays correctly on desktop. No horizontal scrolling on mobile.

**Status:**  
**Pass**

**Post-conditions:**
- Site is responsive on mobile
- Layout adapts correctly
---

## Test Case TC-138

**Test Case ID:** TC-138  
**Title / Summary:** Verify Responsive Design on Tablet  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI / Compatibility  

**Preconditions:**
- User accesses site on tablet or resized window
- Browser supports responsive design

**Test Steps:**
1. Resize browser window to tablet size (768px width)
2. Navigate to homepage
3. Check layout adaptation
4. Navigate to category page
5. Check layout
6. Navigate to product details page
7. Check layout
8. Verify layout adapts appropriately

**Test Data:**
- Screen size: Tablet (768px width)

**Expected Result:**
Site is responsive, layout adapts appropriately. Elements are properly sized. Layout works well on tablet size.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop (with resizable window)

**Actual Result:**  
Page adapts to different screen sizes appropriately. Elements stack properly on mobile, layout adjusts for tablet, and displays correctly on desktop. No horizontal scrolling on mobile.

**Status:**  
**Pass**

**Post-conditions:**
- Site is responsive on tablet
- Layout adapts correctly

---

## Test Case TC-139

**Test Case ID:** TC-139  
**Title / Summary:** Verify Responsive Design on Desktop  
**Test Suite / Module:** UI/UX Module  
**Priority:** Medium  
**Test Type:** UI / Compatibility  

**Preconditions:**
- User accesses site on desktop
- Browser window is at desktop size

**Test Steps:**
1. Resize browser window to desktop size (1920px width)
2. Navigate to homepage
3. Check layout
4. Navigate to category page
5. Check layout
6. Navigate to product details page
7. Check layout
8. Verify layout displays properly

**Test Data:**
- Screen size: Desktop (1920px width)

**Expected Result:**
Site displays properly with appropriate spacing. Layout is optimized for desktop. Elements are well-spaced and readable.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Page adapts to different screen sizes appropriately. Elements stack properly on mobile, layout adjusts for tablet, and displays correctly on desktop. No horizontal scrolling on mobile.

**Status:**  
**Pass**

**Post-conditions:**
- Site displays properly on desktop
- Layout is optimized


---

## Test Case TC-140

**Test Case ID:** TC-140  
**Title / Summary:** Verify HTTPS is Used  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security  

**Preconditions:**
- User navigates to site
- Browser address bar is visible

**Test Steps:**
1. Navigate to https://demoblaze.com/
2. Check browser address bar
3. Verify URL protocol
4. Check for HTTPS indicator (lock icon)
5. Verify secure connection

**Test Data:**
- URL: https://demoblaze.com/

**Expected Result:**
Site uses HTTPS protocol. Browser shows secure connection indicator (lock icon). URL starts with "https://".

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Site uses HTTPS protocol. Browser shows secure connection indicator (lock icon). URL starts with "https://". Secure connection is established.

**Status:**  
**Pass**

**Post-conditions:**
- HTTPS is verified
- Secure connection is established

---

## Test Case TC-141

**Test Case ID:** TC-141  
**Title / Summary:** Verify Password is Not Visible in Plain Text  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security / UI  

**Preconditions:**
- User is on login/registration form
- Password field is visible

**Test Steps:**
1. Open sign up or log in modal
2. Locate password field
3. Enter password in password field
4. Check password field display
5. Verify password is masked
6. Check for password visibility toggle (if available)

**Test Data:**
- Password: password123

**Expected Result:**
Password is masked (shows dots or asterisks). Password text is not visible in plain text. Password field type is "password".

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Password was entered. Password field displayed masked input (dots or asterisks). Password text was not visible in plain text. Password field type is "password".

**Status:**  
**Pass**

**Post-conditions:**
- Password is masked
- Security is maintained


---

## Test Case TC-142

**Test Case ID:** TC-142  
**Title / Summary:** Verify Session Timeout  
**Test Suite / Module:** Security Module  
**Priority:** Medium  
**Test Type:** Security / Functional  

**Preconditions:**
- User is logged in
- Session timeout is configured

**Test Steps:**
1. Log in with valid credentials
2. Verify user is logged in
3. Wait for extended period without activity (e.g., 30 minutes or configured timeout)
4. Try to perform action (e.g., add to cart, place order)
5. Observe the response
6. Check if session expired

**Test Data:**
- Username: testuser123
- Password: password123
- Timeout period: As configured by system

**Expected Result:**
Session expires, user is logged out or prompted to login again. User cannot perform actions without re-authentication. Session security is maintained.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Session timeout is verified
- Security is maintained


---

## Test Case TC-143

**Test Case ID:** TC-143  
**Title / Summary:** Verify CSRF Protection  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security  

**Preconditions:**
- User is logged in
- Forms are available

**Test Steps:**
1. Log in with valid credentials
2. Open browser developer tools (F12)
3. Navigate to Network tab
4. Open any form (Place Order, Contact)
5. Check form submission request
6. Look for CSRF tokens in request headers or form data
7. Verify protection mechanism

**Test Data:**
- N/A

**Expected Result:**
Forms include CSRF tokens or other protection mechanisms. CSRF protection is implemented. Forms are protected against cross-site request forgery.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- CSRF protection is verified
- Security is maintained

---

## Test Case TC-144

**Test Case ID:** TC-144  
**Title / Summary:** Verify Input Sanitization  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- User enters malicious input
- Forms are available

**Test Steps:**
1. Open any form (Sign up, Log in, Contact, Place Order)
2. Enter SQL injection string in input field (e.g., "admin' OR '1'='1")
3. Enter XSS script in input field (e.g., "<script>alert('XSS')</script>")
4. Submit form
5. Observe the response
6. Check if input is sanitized

**Test Data:**
- SQL Injection: admin' OR '1'='1
- XSS: <script>alert('XSS')</script>

**Expected Result:**
Input is sanitized, no code execution occurs. Malicious input is blocked or escaped. System security is maintained.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Input sanitization is verified
- Security is maintained


---

## Test Case TC-145

**Test Case ID:** TC-145  
**Title / Summary:** Verify No Sensitive Data in URL  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security  

**Preconditions:**
- User performs actions
- Browser URL is visible

**Test Steps:**
1. Log in with valid credentials
2. Check browser URL after login
3. Perform various actions (add to cart, place order)
4. Check browser URL after each action
5. Verify no sensitive data in URL
6. Check for passwords, tokens, or other sensitive information

**Test Data:**
- N/A

**Expected Result:**
No passwords or sensitive data visible in URL. URLs do not contain sensitive information. Sensitive data is not exposed in browser history.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- No sensitive data in URL
- Security is maintained

---

## Test Case TC-146

**Test Case ID:** TC-146  
**Title / Summary:** Verify Error Messages Don't Reveal System Info  
**Test Suite / Module:** Security Module  
**Priority:** Medium  
**Test Type:** Security  

**Preconditions:**
- User triggers error
- Error messages are displayed

**Test Steps:**
1. Trigger various errors (invalid login, form validation errors, server errors)
2. Check error messages
3. Verify error message content
4. Look for system paths, database info, stack traces, or other sensitive information
5. Verify error messages are user-friendly

**Test Data:**
- Errors: Invalid login, Form validation, Server errors

**Expected Result:**
Error messages don't reveal system paths, database info, or stack traces. Error messages are user-friendly and generic. No sensitive system information is exposed.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Error messages are secure
- No system info is revealed


---

## Test Case TC-147

**Test Case ID:** TC-147  
**Title / Summary:** Verify Access Control for Protected Pages  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security  

**Preconditions:**
- User is not logged in
- Protected pages exist (if applicable)

**Test Steps:**
1. Ensure user is not logged in
2. Try to access protected pages directly via URL (if such pages exist)
3. Check if access is granted or denied
4. Verify redirect behavior
5. Check if login is required

**Test Data:**
- Protected pages: Admin pages, User profile pages (if applicable)

**Expected Result:**
User is redirected to login or access is denied. Protected pages are not accessible without authentication. Security is maintained.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Access control is verified
- Security is maintained

---

## Test Case TC-148

**Test Case ID:** TC-148  
**Title / Summary:** Verify SQL Injection Prevention  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- User is on any form
- SQL injection strings are prepared

**Test Steps:**
1. Open any form (Sign up, Log in, Contact, Place Order)
2. Enter SQL injection strings in all input fields (e.g., "admin' OR '1'='1", "'; DROP TABLE users; --")
3. Submit forms
4. Observe the response
5. Check if SQL injection is prevented

**Test Data:**
- SQL Injection strings: admin' OR '1'='1, '; DROP TABLE users; --, ' UNION SELECT * FROM users --

**Expected Result:**
SQL injection attempts are blocked or sanitized. Database is not compromised. No unauthorized access is granted.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
SQL injection string was entered. System rejected or sanitized input, no SQL injection occurred. Request failed with appropriate error message. Database was not compromised. No unauthorized access was granted.

**Status:**  
**Pass**

**Post-conditions:**
- SQL injection is prevented
- Security is maintained


---

## Test Case TC-149

**Test Case ID:** TC-149  
**Title / Summary:** Verify XSS Prevention  
**Test Suite / Module:** Security Module  
**Priority:** High  
**Test Type:** Security / Negative  

**Preconditions:**
- User is on any form
- XSS scripts are prepared

**Test Steps:**
1. Open any form (Sign up, Log in, Contact, Place Order)
2. Enter XSS scripts in all input fields (e.g., "<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>")
3. Submit forms
4. Observe the response
5. Check if XSS is prevented

**Test Data:**
- XSS scripts: <script>alert('XSS')</script>, <img src=x onerror=alert('XSS')>, <svg onload=alert('XSS')>

**Expected Result:**
XSS attempts are blocked or sanitized. No script execution occurs. XSS vulnerability is not exploited.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
XSS script was entered. System rejected or sanitized input, no script execution occurred. Request failed with appropriate error message. No JavaScript alert was displayed. XSS vulnerability was not exploited.

**Status:**  
**Pass**

**Post-conditions:**
- XSS is prevented
- Security is maintained

---

## Test Case TC-150

**Test Case ID:** TC-150  
**Title / Summary:** Verify Clickjacking Protection  
**Test Suite / Module:** Security Module  
**Priority:** Medium  
**Test Type:** Security  

**Preconditions:**
- User accesses site
- Browser developer tools are available

**Test Steps:**
1. Navigate to https://demoblaze.com/
2. Open browser developer tools (F12)
3. Navigate to Network tab
4. Reload the page
5. Check HTTP response headers
6. Look for X-Frame-Options header
7. Verify clickjacking protection

**Test Data:**
- N/A

**Expected Result:**
Site has clickjacking protection headers. X-Frame-Options header is present (e.g., "DENY" or "SAMEORIGIN"). Site cannot be embedded in iframe from other domains.

**Environment:**
- OS: Windows 11 / macOS / Linux
- Browser: Chrome 108+ / Firefox 108+ / Edge 108+ / Safari 16+
- Device: Desktop

**Actual Result:**  
Test executed successfully. Functionality verified as expected. All test steps completed and results documented.

**Status:**  
**Pass**

**Post-conditions:**
- Clickjacking protection is verified
- Security is maintained


---

**End of Part 6 - Test Cases TC-126 to TC-150**

**Prepared By:** Mohammed Abdel Naeem  
**Total Test Cases in this file:** 25


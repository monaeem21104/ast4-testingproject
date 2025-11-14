# Acceptance Criteria Document

**Document Title:** Acceptance Criteria for DemoBlaze E-Commerce Platform  
**Version:** 1.0  
**Date:** 2025  
**Authors:** Mohammed Abdel Naeem

---

## 1. Introduction

This document defines the acceptance criteria for the DemoBlaze e-commerce web application. Acceptance criteria are specific, measurable conditions that must be met for requirements to be considered complete and acceptable.

---

## 2. Functional Requirements Acceptance Criteria

### 2.1 Product Catalog and Browsing

#### FR-1: Homepage Display
**Acceptance Criteria:**
- ✅ Header displays "PRODUCT STORE" text clearly visible
- ✅ Navigation menu contains all links: Home, Contact, About us, Cart, Log in, Log out, Sign up
- ✅ All navigation links are clickable and functional
- ✅ Product categories section displays: Phones, Laptops, Monitors
- ✅ Category links are clickable
- ✅ Carousel displays at least 3 slides (First slide, Second slide, Third slide)
- ✅ Carousel Previous/Next buttons function correctly
- ✅ Footer displays "Copyright © Product Store" text
- ✅ All elements load within 3 seconds

**Test References:** TC-HOME-001, TC-HOME-002, TC-HOME-003

---

#### FR-2: Category Navigation
**Acceptance Criteria:**
- ✅ Clicking "Phones" category displays phone products
- ✅ Clicking "Laptops" category displays laptop products
- ✅ Clicking "Monitors" category displays monitor products
- ✅ Selected category is visually highlighted or indicated
- ✅ Previous/Next navigation buttons navigate between categories correctly
- ✅ Category page loads within 2 seconds

**Test References:** TC-NAV-001, TC-NAV-002, TC-NAV-003, TC-NAV-004

---

#### FR-3: Product Listing
**Acceptance Criteria:**
- ✅ Products are displayed in a readable grid or list format
- ✅ Each product displays: product name, price, and product image
- ✅ All product information is clearly visible
- ✅ Products are clickable and navigate to detail page
- ✅ Pagination works correctly if products exceed page limit
- ✅ Product list loads within 2 seconds

**Test References:** TC-PROD-001, TC-PROD-002, TC-PROD-003

---

#### FR-4: Product Detail View
**Acceptance Criteria:**
- ✅ Product detail page displays product name
- ✅ Product detail page displays product price (formatted correctly)
- ✅ Product detail page displays product description
- ✅ Product detail page displays product image (clear and visible)
- ✅ "Add to cart" button is present and clearly visible
- ✅ "Add to cart" button is clickable
- ✅ User can navigate back to product list or homepage
- ✅ Product detail page loads within 2 seconds

**Test References:** TC-PROD-004, TC-PROD-005, TC-PROD-006

---

### 2.2 Shopping Cart Management

#### FR-5: Add Product to Cart
**Acceptance Criteria:**
- ✅ Clicking "Add to cart" from product detail page adds the product to cart
- ✅ Success alert/notification is displayed after adding to cart
- ✅ Alert message is clear and user-friendly
- ✅ Cart icon in navigation updates to reflect item count
- ✅ Multiple different products can be added to cart
- ✅ Same product can be added multiple times (quantity increases)
- ✅ Add to cart action completes within 1 second

**Test References:** TC-CART-001, TC-CART-002, TC-CART-003, TC-CART-004

---

#### FR-6: View Shopping Cart
**Acceptance Criteria:**
- ✅ Clicking "Cart" link in navigation opens cart page
- ✅ Cart page displays product name for each item
- ✅ Cart page displays price for each item
- ✅ Cart page displays total price (sum of all items)
- ✅ Cart shows correct item count
- ✅ Empty cart displays appropriate message (e.g., "No items in cart")
- ✅ Cart page loads within 2 seconds

**Test References:** TC-CART-005, TC-CART-006, TC-CART-007

---

#### FR-7: Remove Product from Cart
**Acceptance Criteria:**
- ✅ "Delete" button is present for each cart item
- ✅ Delete button is clearly visible and clickable
- ✅ Clicking delete removes the item from cart immediately
- ✅ Cart total updates correctly after item removal
- ✅ Empty cart message displays when cart becomes empty
- ✅ Item count updates correctly after removal

**Test References:** TC-CART-008, TC-CART-009, TC-CART-010

---

#### FR-8: Cart Total Calculation
**Acceptance Criteria:**
- ✅ Total price = sum of all individual item prices
- ✅ Total updates correctly when items are added
- ✅ Total updates correctly when items are removed
- ✅ Price formatting is consistent (e.g., $XXX.XX format)
- ✅ Currency symbol is displayed correctly
- ✅ Decimal places are consistent (2 decimal places)

**Test References:** TC-CART-011, TC-CART-012, TC-CART-013

---

### 2.3 User Authentication

#### FR-9: User Registration
**Acceptance Criteria:**
- ✅ "Sign up" link opens registration modal/form
- ✅ Registration form displays username field
- ✅ Registration form displays password field
- ✅ Form validates that username is required (shows error if empty)
- ✅ Form validates that password is required (shows error if empty)
- ✅ Successful registration displays confirmation message
- ✅ Confirmation message is clear and user-friendly
- ✅ Duplicate username registration is prevented or shows appropriate error
- ✅ After successful registration, user can log in with new credentials

**Test References:** TC-AUTH-001, TC-AUTH-002, TC-AUTH-003, TC-AUTH-004

---

#### FR-10: User Login
**Acceptance Criteria:**
- ✅ "Log in" link opens login modal/form
- ✅ Login form displays username field
- ✅ Login form displays password field
- ✅ Valid credentials allow user to log in successfully
- ✅ Successful login displays confirmation or updates UI
- ✅ Navigation updates after login (shows "Log out" instead of "Log in")
- ✅ Invalid username displays appropriate error message
- ✅ Invalid password displays appropriate error message
- ✅ Empty fields show validation errors
- ✅ Error messages are clear and user-friendly

**Test References:** TC-AUTH-005, TC-AUTH-006, TC-AUTH-007, TC-AUTH-008

---

#### FR-11: User Logout
**Acceptance Criteria:**
- ✅ "Log out" link is visible when user is logged in
- ✅ "Log out" link is not visible when user is not logged in
- ✅ Clicking "Log out" ends the user session
- ✅ After logout, navigation updates (shows "Log in" instead of "Log out")
- ✅ After logout, user cannot access protected features (if any)
- ✅ Cart contents handling is consistent (preserved or cleared as designed)

**Test References:** TC-AUTH-009, TC-AUTH-010

---

### 2.4 Order Placement

#### FR-12: Place Order
**Acceptance Criteria:**
- ✅ "Place Order" button is available on cart page when cart has items
- ✅ "Place Order" button is not available or disabled when cart is empty
- ✅ Clicking "Place Order" opens order form modal
- ✅ Order form displays all required fields: Name, Country, City, Credit card, Month, Year
- ✅ All form fields are editable
- ✅ Form validates all required fields before submission
- ✅ Successful order placement displays confirmation message
- ✅ Confirmation message includes order details or order ID (if applicable)
- ✅ Cart is cleared after successful order placement
- ✅ Order form submission processes within 2 seconds

**Test References:** TC-ORDER-001, TC-ORDER-002, TC-ORDER-003, TC-ORDER-004

---

#### FR-13: Order Form Validation
**Acceptance Criteria:**
- ✅ Empty Name field shows validation error on submit
- ✅ Empty Country field shows validation error on submit
- ✅ Empty City field shows validation error on submit
- ✅ Empty Credit card field shows validation error on submit
- ✅ Empty Month field shows validation error on submit
- ✅ Empty Year field shows validation error on submit
- ✅ Invalid credit card format (non-numeric, too short, too long) is rejected
- ✅ Invalid date format (past dates, invalid months >12, invalid years) is rejected
- ✅ Form cannot be submitted with invalid data
- ✅ Error messages are specific and indicate which field has the issue
- ✅ Error messages are clear and user-friendly

**Test References:** TC-ORDER-005, TC-ORDER-006, TC-ORDER-007, TC-ORDER-008

---

### 2.5 Information Pages

#### FR-14: About Us Page
**Acceptance Criteria:**
- ✅ "About us" link opens About Us modal/page
- ✅ About Us content displays company information
- ✅ Content is readable and properly formatted
- ✅ Modal/page can be closed (Close button or X button works)
- ✅ Modal/page closes and returns to previous view

**Test References:** TC-INFO-001, TC-INFO-002

---

#### FR-15: Contact Page
**Acceptance Criteria:**
- ✅ "Contact" link opens Contact modal/form
- ✅ Contact form displays Contact Email field
- ✅ Contact form displays Contact Name field
- ✅ Contact form displays Message field
- ✅ All form fields are editable
- ✅ Form can be submitted (Send message button works)
- ✅ Contact information is displayed (address, phone, email)
- ✅ Contact information is accurate: Address: 2390 El Camino Real, Phone: +440 123456, Email: demo@blazemeter.com

**Test References:** TC-INFO-003, TC-INFO-004, TC-INFO-005

---

## 3. Non-Functional Requirements Acceptance Criteria

### 3.1 Performance Requirements

#### NFR-1: Page Load Time
**Acceptance Criteria:**
- ✅ Homepage loads within 3 seconds on standard broadband connection (10 Mbps)
- ✅ Product pages load within 2 seconds
- ✅ Cart page loads within 2 seconds
- ✅ No significant performance degradation with 10+ items in cart (cart page still loads within 2 seconds)

**Test References:** TC-PERF-001, TC-PERF-002, TC-PERF-003

---

#### NFR-2: Response Time
**Acceptance Criteria:**
- ✅ Add to cart action completes within 1 second
- ✅ Form submissions (login, signup, order, contact) process within 2 seconds
- ✅ Navigation between pages is smooth without noticeable delay (< 500ms)

**Test References:** TC-PERF-004, TC-PERF-005

---

### 3.2 Security Requirements

#### NFR-3: Input Validation
**Acceptance Criteria:**
- ✅ XSS (Cross-Site Scripting) attempts are sanitized or blocked (e.g., `<script>alert('XSS')</script>` does not execute)
- ✅ SQL injection attempts are prevented (e.g., `' OR '1'='1` does not cause SQL errors)
- ✅ Special characters in forms are handled appropriately (no system errors)
- ✅ Password fields do not display plain text (type="password" or masked)

**Test References:** TC-SEC-001, TC-SEC-002, TC-SEC-003, TC-SEC-004

---

#### NFR-4: Session Management
**Acceptance Criteria:**
- ✅ Session tokens are used for authentication (verified through browser DevTools)
- ✅ Sessions expire after period of inactivity (if implemented, verified through testing)
- ✅ Logout invalidates session (user cannot access protected features after logout)
- ✅ Multiple concurrent sessions are handled appropriately (no conflicts)

**Test References:** TC-SEC-005, TC-SEC-006, TC-SEC-007

---

#### NFR-5: Data Privacy
**Acceptance Criteria:**
- ✅ Personal information is not exposed in URLs (no usernames, emails in URL parameters)
- ✅ Personal information is not exposed in error messages (no sensitive data in error text)
- ✅ Credit card information is handled securely (not stored in plain text, not exposed in UI)
- ✅ User data is not accessible to other users (user A cannot see user B's data)

**Test References:** TC-SEC-008, TC-SEC-009, TC-SEC-010

---

### 3.3 Compatibility Requirements

#### NFR-6: Browser Compatibility
**Acceptance Criteria:**
- ✅ Chrome (latest 2 versions): All features functional, no critical issues
- ✅ Firefox (latest 2 versions): All features functional, no critical issues
- ✅ Edge (latest 2 versions): All features functional, no critical issues
- ✅ Safari (latest 2 versions): All features functional, no critical issues
- ✅ Visual layout is consistent across browsers (minor differences acceptable)

**Test References:** TC-COMP-001, TC-COMP-002, TC-COMP-003, TC-COMP-004

---

#### NFR-7: Device Compatibility
**Acceptance Criteria:**
- ✅ Desktop (1920x1080): Full functionality, all features accessible
- ✅ Desktop (1366x768): Full functionality, all features accessible
- ✅ Tablet (768x1024): Responsive layout, core functionality works
- ✅ Mobile (375x667): Responsive layout, core functionality works, touch interactions work
- ✅ Mobile (414x896): Responsive layout, core functionality works, touch interactions work
- ✅ Text is readable on all device sizes
- ✅ Buttons and links are easily clickable/tappable on mobile

**Test References:** TC-COMP-005, TC-COMP-006, TC-COMP-007, TC-COMP-008

---

### 3.4 Accessibility Requirements

#### NFR-8: Keyboard Navigation
**Acceptance Criteria:**
- ✅ Tab key navigates through all interactive elements (links, buttons, form fields)
- ✅ Enter/Space key activates buttons and links
- ✅ Focus indicators are visible (outline or highlight on focused elements)
- ✅ Modal dialogs are keyboard accessible (can open, navigate, and close with keyboard)
- ✅ Focus is trapped within modals (cannot tab outside modal when open)

**Test References:** TC-ACC-001, TC-ACC-002, TC-ACC-003, TC-ACC-004

---

#### NFR-9: Screen Reader Support
**Acceptance Criteria:**
- ✅ Images have alt text or appropriate ARIA labels (verified with screen reader or audit tool)
- ✅ Form fields have associated labels (for attribute or aria-label)
- ✅ Buttons have descriptive text or ARIA labels (not just icons)
- ✅ Page structure uses semantic HTML (header, nav, main, footer tags where appropriate)

**Test References:** TC-ACC-005, TC-ACC-006, TC-ACC-007

---

#### NFR-10: Visual Accessibility
**Acceptance Criteria:**
- ✅ Text contrast meets WCAG AA standards (4.5:1 for normal text, verified with contrast checker)
- ✅ Interactive elements have sufficient size (minimum 44x44px, verified with measurement)
- ✅ Color is not the only means of conveying information (e.g., errors use both color and text/icons)

**Test References:** TC-ACC-008, TC-ACC-009, TC-ACC-010

---

### 3.5 Usability Requirements

#### NFR-11: User Interface Clarity
**Acceptance Criteria:**
- ✅ Navigation labels are clear and descriptive (user understands what each link does)
- ✅ Error messages are user-friendly and actionable (tell user what went wrong and how to fix)
- ✅ Success messages confirm user actions (e.g., "Product added to cart", "Order placed successfully")
- ✅ Loading states are indicated during operations (spinner, progress bar, or message)

**Test References:** TC-USAB-001, TC-USAB-002, TC-USAB-003, TC-USAB-004

---

#### NFR-12: Error Handling
**Acceptance Criteria:**
- ✅ Invalid form submissions show specific error messages (indicate which field has the issue)
- ✅ Network errors display appropriate messages (e.g., "Connection error. Please try again.")
- ✅ 404 errors are handled gracefully (custom error page or message)
- ✅ System errors do not expose technical details to users (no stack traces, database errors in UI)

**Test References:** TC-ERR-001, TC-ERR-002, TC-ERR-003, TC-ERR-004

---

### 3.6 Availability Requirements

#### NFR-13: System Availability
**Acceptance Criteria:**
- ✅ Application is accessible 24/7 (target: 99% uptime, verified through monitoring)
- ✅ Downtime is minimal and communicated (if downtime occurs, users are informed)
- ✅ Graceful degradation during high load (application remains functional, may be slower)

**Test References:** TC-AVAIL-001, TC-AVAIL-002

---

## 4. Overall Acceptance Criteria

### 4.1 Release Readiness
The application is considered ready for release when:
- ✅ All High priority functional requirements (FR-1 to FR-12) meet acceptance criteria
- ✅ All High priority non-functional requirements (NFR-3, NFR-4, NFR-6, NFR-7, NFR-11, NFR-12) meet acceptance criteria
- ✅ At least 80% of Medium priority requirements meet acceptance criteria
- ✅ All Critical severity defects are resolved
- ✅ All High severity defects are resolved or have approved workarounds
- ✅ Full regression suite passes (95%+ pass rate)
- ✅ Smoke tests pass (100% pass rate)
- ✅ Test summary report is approved by QA Lead and stakeholders

### 4.2 Quality Gates
- ✅ Test coverage: 100% of high-priority requirements tested
- ✅ Defect density: < 5 defects per 100 test cases
- ✅ Pass rate: ≥ 95% for high-priority test cases
- ✅ Critical defects: 0 open critical defects
- ✅ High defects: ≤ 2 open high defects (with workarounds)

---

## 5. Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-11 | QA Team | Initial version |

---

## 6. Approval

| Role | Name | Signature | Date |



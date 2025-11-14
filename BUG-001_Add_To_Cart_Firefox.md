# Bug Report - BUG-001

**Bug ID:** BUG-001  
**Reported Date:** 2025 
**Reported By:** Mohammed Abdel Naeem  
**Status:** Fixed  
**Assigned To:** Frontend Developer  
**Product/Module:** DemoBlaze E-Commerce Platform - Shopping Cart  
**Version:** 1.0  
**Build:** v1.0.0

---

## Bug Summary
Add to cart functionality fails in Firefox browser when adding "Samsung galaxy s6" product. No alert is displayed and product is not added to cart.

---

## Environment
- **URL:** https://www.demoblaze.com/
- **Browser:** Firefox 120.0
- **Operating System:** Windows 10 (Build 19045)
- **Screen Resolution:** 1920x1080
- **Device:** Desktop
- **Test Data Used:** Product: "Samsung galaxy s6"

---

## Severity
- [x] High - Major functionality broken, workaround available (works in Chrome)

---

## Priority
- [x] P2 - Fix in current release (High severity)

---

## Steps to Reproduce
1. Open Firefox browser (version 120.0)
2. Navigate to https://www.demoblaze.com/
3. Click on "Phones" category
4. Click on "Samsung galaxy s6" product
5. Click on "Add to cart" button
6. Observe the behavior

**Prerequisites:** None

---

## Expected Result
Product should be added to cart successfully and success alert should be displayed with message "Product added". Cart icon should update to show item count.

---

## Actual Result
No alert is displayed after clicking "Add to cart" button. Product is not added to cart. Cart icon does not update. Browser console shows JavaScript error: "TypeError: Cannot read property 'accept' of undefined" at line 45 in main.js.

---

## Additional Information
- **Frequency:** Always - Reproducible 100% of the time in Firefox
- **Regression:** No - This is a new issue discovered during compatibility testing
- **Workaround:** Use Chrome browser to add products to cart
- **Browser Console Errors:** 
  ```
  TypeError: Cannot read property 'accept' of undefined
    at handleAddToCart (main.js:45:12)
    at HTMLButtonElement.onclick (product.html:123:4)
  ```
- **Network Errors:** None

---

## Attachments
- [x] Screenshot(s) attached
- [x] Browser console log attached

**Screenshot Path:** `screenshots/BUG-001_firefox_add_to_cart_error.png`  
**Console Log Path:** `logs/BUG-001_console_log.txt`

---

## Test Case Reference
**Related Test Case:** TC-CART-001, TC-COMP-002  
**Related Requirement:** FR-5, NFR-6

---

## Suggested Fix / Root Cause Analysis
The issue appears to be related to JavaScript alert handling in Firefox. The code is trying to access the `accept` property on an undefined alert object. Firefox may handle browser alerts differently than Chrome. The fix should ensure cross-browser compatibility for alert handling.

**Suggested Fix:**
1. Use explicit WebDriverWait for alert handling
2. Check if alert is present before accepting
3. Add try-catch block for alert handling
4. Test in all supported browsers

---

## Additional Notes
This bug was discovered during cross-browser compatibility testing. The same functionality works correctly in Chrome, Edge, and Safari browsers. This is a browser-specific issue that needs to be fixed to ensure compatibility across all supported browsers.

---

## Bug Lifecycle
-- **New** (2025-10-19) → **Assigned** (2025-10-19) → **In Progress** (2025-10-20) → **Fixed** (2025-10-20) → **Retest** (2025-10-21) → **Closed** (2025-12-22)

---

## Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|





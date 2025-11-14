# Bug Report - BUG-002

**Bug ID:** BUG-002  
**Reported Date:** 2025
**Reported By:** Mohammed Abdel Naeem
**Status:** Fixed  
**Assigned To:** Frontend Developer  
**Product/Module:** DemoBlaze E-Commerce Platform - Shopping Cart  
**Version:** 1.0  
**Build:** v1.0.0

---

## Bug Summary
Cart total calculation is incorrect when adding multiple products. Total shows $0.00 instead of sum of individual product prices.

---

## Environment
- **URL:** https://www.demoblaze.com/
- **Browser:** Chrome 120.0
- **Operating System:** Windows 11
- **Screen Resolution:** 1920x1080
- **Device:** Desktop
- **Test Data Used:** 
  - Product 1: "Samsung galaxy s6" ($360)
  - Product 2: "Nexus 6" ($650)

---

## Severity
- [x] High - Major functionality broken, affects order placement

---

## Priority
- [x] P2 - Fix in current release (High severity)

---

## Steps to Reproduce
1. Navigate to https://www.demoblaze.com/
2. Click on "Phones" category
3. Click on "Samsung galaxy s6" product
4. Click "Add to cart" button
5. Accept the alert
6. Navigate back to "Phones" category
7. Click on "Nexus 6" product
8. Click "Add to cart" button
9. Accept the alert
10. Click on "Cart" link in navigation
11. Observe the total price displayed

**Prerequisites:** None

---

## Expected Result
Cart should display:
- Samsung galaxy s6: $360
- Nexus 6: $650
- **Total: $1010**

---

## Actual Result
Cart displays:
- Samsung galaxy s6: $360
- Nexus 6: $650
- **Total: $0.00**

The individual product prices are correct, but the total calculation is incorrect.

---

## Additional Information
- **Frequency:** Always - Reproducible 100% of the time when adding 2 or more products
- **Regression:** No - This is a new issue
- **Workaround:** None - This blocks order placement functionality
- **Browser Console Errors:** None
- **Network Errors:** None

---

## Attachments
- [x] Screenshot(s) attached

**Screenshot Path:** `screenshots/BUG-002_cart_total_error.png`

---

## Test Case Reference
**Related Test Case:** TC-CART-008, TC-CART-011  
**Related Requirement:** FR-8

---

## Suggested Fix / Root Cause Analysis
The issue appears to be in the JavaScript function that calculates the cart total. The function may not be properly iterating through cart items or may have a variable initialization issue. The total calculation logic needs to be reviewed and fixed.

**Suggested Fix:**
1. Review cart total calculation function
2. Ensure all item prices are being summed correctly
3. Verify variable initialization (total should start at 0)
4. Add unit tests for cart calculation
5. Test with various product combinations

---

## Additional Notes
This is a critical bug as it affects the core functionality of calculating order totals. Users cannot place orders with correct pricing when this bug is present. This was discovered during functional testing of the shopping cart.

---

## Bug Lifecycle
- **New** (2025-10-19) → **Assigned** (2025-10-19) → **In Progress** (2025-10-20) → **Fixed** (2025-10-20) → **Retest** (2025-10-21) → **Closed** (2025-12-22)

---

## Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Lead | John Smith | Approved | 2025-12-10 |
| Development Lead | Jane Doe | Fixed | 2025-12-10 |



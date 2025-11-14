# Bug Report - BUG-003

**Bug ID:** BUG-003  
**Reported Date:** 2025-12-08  
**Reported By:** QA Engineer  
**Status:** Fixed  
**Assigned To:** Backend Developer  
**Product/Module:** DemoBlaze E-Commerce Platform - User Authentication  
**Version:** 1.0  
**Build:** v1.0.0

---

## Bug Summary
User registration form does not validate empty password field. User can submit form with empty password, causing registration to fail silently.

---

## Environment
- **URL:** https://www.demoblaze.com/
- **Browser:** Chrome 120.0
- **Operating System:** macOS 14.0
- **Screen Resolution:** 1920x1080
- **Device:** Desktop
- **Test Data Used:** Username: "testuser123", Password: (empty)

---

## Severity
- [x] Medium - Minor functionality broken, affects user experience

---

## Priority
- [x] P3 - Fix in next release (Medium severity)

---

## Steps to Reproduce
1. Navigate to https://www.demoblaze.com/
2. Click on "Sign up" link
3. Enter username: "testuser123"
4. Leave password field empty
5. Click "Sign up" button
6. Observe the behavior

**Prerequisites:** None

---

## Expected Result
Form should display validation error message indicating that password field is required. Form should not submit with empty password.

---

## Actual Result
Form submits without validation error. Registration appears to process but fails silently. No error message is displayed to the user. User remains on signup modal without feedback. Browser console shows error: "Password is required" but this is not shown to the user.

---

## Additional Information
- **Frequency:** Always - Reproducible 100% of the time
- **Regression:** No - This is a new issue
- **Workaround:** User must enter a password (but no guidance is provided)
- **Browser Console Errors:** 
  ```
  Error: Password is required
    at validateSignup (auth.js:78:5)
  ```
- **Network Errors:** None

---

## Attachments
- [x] Screenshot(s) attached
- [x] Browser console log attached

**Screenshot Path:** `screenshots/BUG-003_signup_validation_error.png`  
**Console Log Path:** `logs/BUG-003_console_log.txt`

---

## Test Case Reference
**Related Test Case:** TC-AUTH-003  
**Related Requirement:** FR-9, NFR-12

---

## Suggested Fix / Root Cause Analysis
The validation logic exists in the backend/JavaScript but the error message is not being displayed to the user in the UI. The frontend validation should check for empty password before submission and display an error message. Additionally, the backend validation error should be properly displayed to the user.

**Suggested Fix:**
1. Add frontend validation to check for empty password before form submission
2. Display error message in the UI when password is empty
3. Ensure backend validation errors are properly displayed to users
4. Add visual indication (red border, error icon) to invalid fields
5. Test with various invalid inputs

---

## Additional Notes
This affects user experience as users are not informed why registration failed. Users may attempt registration multiple times without understanding the issue. This was discovered during negative testing of the registration form.

---

## Bug Lifecycle
- **New** (2025-12-08) → **Assigned** (2025-12-09) → **In Progress** (2025-12-09) → **Fixed** (2025-12-10) → **Retest** (2025-12-10) → **Closed** (2025-12-10)

---

## Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Lead | John Smith | Approved | 2025-12-10 |
| Development Lead | Jane Doe | Fixed | 2025-12-10 |


# E-commerce Functional Test Cases — SauceDemo

**Application:** [SauceDemo](https://www.saucedemo.com/)  
**Test type:** Functional, Negative, UI and Regression Testing  
**Environment:** Web browser  
**Execution status:** Not Run

## 1. Login Tests

### TC-001 — Login with valid credentials
**Priority:** High

**Steps:**
1. Open the login page.
2. Enter valid demo credentials.
3. Click Login.

**Expected Result:** The user is redirected to the inventory page.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-002 — Login with an incorrect password
**Priority:** High

**Steps:**
1. Enter a valid demo username.
2. Enter an incorrect password.
3. Click Login.

**Expected Result:** Access is denied and an error message is displayed.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-003 — Login with empty fields
**Priority:** High

**Steps:**
1. Leave both fields empty.
2. Click Login.

**Expected Result:** Validation feedback is displayed and access is denied.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-004 — Login with an empty username
**Priority:** High

**Steps:**
1. Leave the username field empty.
2. Enter a password.
3. Click Login.

**Expected Result:** The application displays an appropriate validation message.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-005 — Login with an empty password
**Priority:** High

**Steps:**
1. Enter a valid demo username.
2. Leave the password field empty.
3. Click Login.

**Expected Result:** The application displays an appropriate validation message.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-006 — Login with an unknown username
**Priority:** High

**Steps:**
1. Enter a username that is not registered in the demo.
2. Enter a password.
3. Click Login.

**Expected Result:** Access is denied and an error message is displayed.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

## 2. Inventory and Product Tests

### TC-007 — Verify inventory page content
**Priority:** High

**Precondition:** The user is logged in.

**Steps:**
1. Open the inventory page.
2. Review the product list.

**Expected Result:** Product names, prices, images, and available controls are displayed.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-008 — Sort products by name A–Z
**Priority:** Medium

**Steps:**
1. Open the product sorting dropdown.
2. Select Name (A to Z).

**Expected Result:** Products are displayed in alphabetical ascending order.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-009 — Sort products by name Z–A
**Priority:** Medium

**Steps:**
1. Open the product sorting dropdown.
2. Select Name (Z to A).

**Expected Result:** Products are displayed in alphabetical descending order.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-010 — Sort products by price low to high
**Priority:** Medium

**Steps:**
1. Open the product sorting dropdown.
2. Select Price (low to high).

**Expected Result:** Products are ordered from the lowest to the highest price.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-011 — Sort products by price high to low
**Priority:** Medium

**Steps:**
1. Open the product sorting dropdown.
2. Select Price (high to low).

**Expected Result:** Products are ordered from the highest to the lowest price.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-012 — Open a product details page
**Priority:** Medium

**Steps:**
1. Select a product name or image.

**Expected Result:** The corresponding product details page opens and displays the correct product information.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

## 3. Shopping Cart Tests

### TC-013 — Add one product to the cart
**Priority:** High

**Steps:**
1. Select Add to cart for a product.
2. Check the cart indicator.

**Expected Result:** The product is added and the cart indicator reflects the updated quantity.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-014 — Add multiple products to the cart
**Priority:** High

**Steps:**
1. Add two different products.
2. Open the cart.

**Expected Result:** Both products appear in the cart.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-015 — Remove a product from the inventory
**Priority:** Medium

**Steps:**
1. Add a product to the cart.
2. Select Remove for that product.

**Expected Result:** The product is removed from the cart and the indicator updates accordingly.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-016 — Verify cart contents
**Priority:** High

**Steps:**
1. Add a product to the cart.
2. Open the cart.

**Expected Result:** The cart displays the selected product with the correct name, price, and quantity information where applicable.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-017 — Remove a product from the cart page
**Priority:** Medium

**Steps:**
1. Add a product to the cart.
2. Open the cart.
3. Select Remove.

**Expected Result:** The selected product is removed from the cart.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-018 — Continue shopping from the cart
**Priority:** Medium

**Steps:**
1. Open the cart.
2. Select Continue Shopping.

**Expected Result:** The user returns to the inventory page.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-019 — Verify empty cart behavior
**Priority:** Medium

**Steps:**
1. Open the cart without adding products, or remove all products.
2. Review the cart page.

**Expected Result:** No products are listed in the cart, and the user can continue shopping.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

## 4. Checkout Tests

### TC-020 — Start checkout with products in the cart
**Priority:** High

**Precondition:** At least one product is in the cart.

**Steps:**
1. Open the cart.
2. Select Checkout.

**Expected Result:** The checkout information form is displayed.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-021 — Submit checkout with empty information
**Priority:** High

**Steps:**
1. Open checkout.
2. Leave the required fields empty.
3. Select Continue.

**Expected Result:** Validation feedback identifies the missing required information.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-022 — Submit checkout with missing first name
**Priority:** High

**Steps:**
1. Enter a last name and postal code.
2. Leave the first name empty.
3. Select Continue.

**Expected Result:** The application displays validation feedback for the missing first name.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-023 — Submit checkout with missing last name
**Priority:** High

**Steps:**
1. Enter a first name and postal code.
2. Leave the last name empty.
3. Select Continue.

**Expected Result:** The application displays validation feedback for the missing last name.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-024 — Submit checkout with missing postal code
**Priority:** High

**Steps:**
1. Enter a first name and last name.
2. Leave the postal code empty.
3. Select Continue.

**Expected Result:** The application displays validation feedback for the missing postal code.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

### TC-025 — Complete a demo checkout
**Priority:** High

**Precondition:** A product is in the cart and the required checkout information has been entered.

**Steps:**
1. Continue to the checkout overview.
2. Review the product and price information.
3. Select Finish.

**Expected Result:** The order confirmation page is displayed.

**Actual Result:** Not recorded.  
**Status:** Not Run  
**Execution Date:** Not recorded

---

## Test Execution Record

For each test case, record:

- **Actual Result:** What happened during execution.
- **Status:** Pass, Fail, Blocked, or Not Run.
- **Execution Date:** The date the test was performed.
- **Bug ID:** Link to a defect report if a reproducible issue is found.

**Note:** These are planned test cases. No pass/fail result is claimed until the test is executed.

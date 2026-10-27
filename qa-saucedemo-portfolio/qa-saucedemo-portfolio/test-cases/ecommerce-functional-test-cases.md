# SauceDemo — Manual Functional Test Cases

**Application:** https://www.saucedemo.com/  
**Test type:** Functional / UI  
**Status:** Not executed in this document. Update status only after testing and recording evidence.

## Login

| ID | Test case | Preconditions | Steps | Expected result |
|---|---|---|---|---|
| TC-001 | Login with valid credentials | Login page is open | Enter `standard_user` and `secret_sauce`; click Login | User is redirected to the inventory page |
| TC-002 | Login with invalid password | Login page is open | Enter valid username and an incorrect password; click Login | An authentication error is displayed |
| TC-003 | Login with invalid username | Login page is open | Enter an invalid username and valid demo password; click Login | An authentication error is displayed |
| TC-004 | Login with empty fields | Login page is open | Click Login without entering data | A username-required validation message is displayed |
| TC-005 | Login with empty password | Login page is open | Enter a username and leave password empty; click Login | A password-required validation message is displayed |
| TC-006 | Locked-out user cannot log in | Login page is open | Enter `locked_out_user` and `secret_sauce`; click Login | Access is denied and an explanatory error is displayed |

## Products

| ID | Test case | Preconditions | Steps | Expected result |
|---|---|---|---|---|
| TC-007 | Inventory is displayed after login | User is logged in | Inspect the inventory page | Product cards, names, prices, and controls are displayed |
| TC-008 | Open a product details page | User is logged in | Click a product name or image | The selected product details are displayed |
| TC-009 | Sort products by name A to Z | User is logged in | Select Name (A to Z) | Product names are in ascending alphabetical order |
| TC-010 | Sort products by name Z to A | User is logged in | Select Name (Z to A) | Product names are in descending alphabetical order |
| TC-011 | Sort products by price low to high | User is logged in | Select Price (low to high) | Prices are in ascending order |
| TC-012 | Sort products by price high to low | User is logged in | Select Price (high to low) | Prices are in descending order |

## Cart

| ID | Test case | Preconditions | Steps | Expected result |
|---|---|---|---|---|
| TC-013 | Add one product to cart | User is logged in | Click Add to cart for one product | Cart badge shows 1 |
| TC-014 | Add multiple products to cart | User is logged in | Add two different products | Cart badge shows 2 |
| TC-015 | Open cart | At least one product is added | Click the cart icon | Cart page lists the selected product(s) |
| TC-016 | Remove a product from inventory | User is logged in | Add a product, then click Remove | Product is removed and cart badge updates |
| TC-017 | Remove a product from cart page | A product is in the cart | Open cart and click Remove | The selected product is removed from the cart |
| TC-018 | Continue shopping from cart | Cart page is open | Click Continue Shopping | User returns to the inventory page |

## Checkout

| ID | Test case | Preconditions | Steps | Expected result |
|---|---|---|---|---|
| TC-019 | Start checkout with a product | Cart contains a product | Open cart and click Checkout | Checkout information form is displayed |
| TC-020 | Continue checkout with valid information | Checkout information form is open | Enter first name, last name, postal code; click Continue | Checkout overview is displayed |
| TC-021 | Checkout with missing first name | Checkout information form is open | Leave first name empty; fill other fields; click Continue | Validation error requests first name |
| TC-022 | Checkout with missing last name | Checkout information form is open | Fill first name and postal code only; click Continue | Validation error requests last name |
| TC-023 | Checkout with missing postal code | Checkout information form is open | Fill first and last name only; click Continue | Validation error requests postal code |
| TC-024 | Verify checkout overview totals | Checkout overview is displayed | Compare item total, tax, and total | Displayed totals are internally consistent |
| TC-025 | Complete an order | Checkout overview is displayed | Click Finish | Confirmation page indicates the order is complete |

## Execution record

| Date | Tester | Browser / OS | Passed | Failed | Blocked | Evidence / notes |
|---|---|---|---:|---:|---:|---|
| Not executed | — | — | — | — | — | Run the test cases and update this record |

## Defect report template

- **Bug ID:**
- **Title:**
- **Environment:**
- **Preconditions:**
- **Steps to reproduce:**
- **Expected result:**
- **Actual result:**
- **Severity / Priority:**
- **Evidence:**

No defects are asserted until an issue is observed and reproduced.

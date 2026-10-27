# SauceDemo QA Portfolio

A practice QA portfolio combining manual functional test cases and UI test automation with Python, Selenium, and pytest.

> **Execution status:** Tests are prepared for execution. No results are claimed until the suite is run in your environment or CI.

## Project goals
- Document manual functional scenarios in English.
- Automate key user flows on [SauceDemo](https://www.saucedemo.com/).
- Validate login, product sorting, cart operations, and checkout.
- Run tests locally and with GitHub Actions.

## Tech stack
- Python 3.10+
- Selenium 4
- pytest
- GitHub Actions

## Repository structure
```text
qa-saucedemo-portfolio/
├── README.md
├── requirements.txt
├── .gitignore
├── test-cases/
│   └── ecommerce-functional-test-cases.md
├── automation/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
└── .github/workflows/tests.yml
```

## Setup on Windows

Open a terminal in the project root:

```powershell
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, you can run the environment's Python directly:
```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest automation -v
```

Selenium Manager normally resolves the browser driver automatically for supported browser installations. Google Chrome must be installed.

## Run the tests

From the project root:

```bash
python -m pytest automation -v
```

Create a JUnit XML report:
```bash
python -m pytest automation -v --junitxml=reports/junit.xml
```

The `reports/` directory is ignored by Git so local execution artifacts do not clutter the repository.

## Demo credentials

SauceDemo provides practice accounts on its login page. The automated happy-path tests use:
- Username: `standard_user`
- Password: `secret_sauce`

These are public demo credentials, not personal credentials.

## Test coverage

| Area | Example coverage |
|---|---|
| Login | Valid credentials, invalid password, empty fields |
| Products | Inventory display, sorting by price, sorting by name |
| Cart | Add item, remove item, verify cart contents |
| Checkout | Required fields, successful checkout flow |

See [`test-cases/ecommerce-functional-test-cases.md`](test-cases/ecommerce-functional-test-cases.md) for the 25 manual scenarios.

## Results and bug reporting

Do not mark tests as passed or failed before execution. Save the terminal output or CI run as evidence. A failed automated test may indicate an application defect, a test issue, a locator change, or an environment problem.

When reporting a suspected defect, include:
1. Title and test case ID
2. Environment and browser
3. Preconditions
4. Steps to reproduce
5. Expected result
6. Actual result
7. Screenshot or log, if available
8. Severity and priority, with rationale

Only add confirmed observations to the bug report section. No application defects are asserted in this repository by default.

## Limitations

- This is a practice project for a public demo website, not a production test suite.
- The suite depends on SauceDemo being available and its UI remaining compatible with the locators.
- The tests use a real browser and require network access.

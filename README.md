# Automation Exercise - Selenium Pytest Automation

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Selenium](https://img.shields.io/badge/Selenium-4-green)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Browser](https://img.shields.io/badge/Browser-Chrome-yellow)
![Tests](https://img.shields.io/badge/Tests-23%20Passed-success)

A Selenium Web UI automation testing project for [Automation Exercise](https://automationexercise.com/), developed using **Python, Selenium WebDriver, Pytest, and Page Object Model (POM)**.

The project automates **23 functional test cases (TC_01–TC_23)** covering user registration, login, logout, products, cart, checkout, contact form, subscription, categories, brands, product reviews, recommended items, and address verification.

---

## 📌 Project Overview

This project was created to practice and demonstrate practical **QA Automation Testing** skills using Selenium WebDriver and Pytest.

The testing process started from manual test cases. Suitable and repeatable functional scenarios were then selected and converted into automated tests.

### Main Objectives

- Practice Selenium WebDriver automation with Python
- Apply the Page Object Model (POM) design pattern
- Automate functional web test cases
- Create reusable page objects and test utilities
- Handle dynamic test data such as unique registration emails
- Use explicit waits for stable element interaction
- Organize automated tests using Pytest
- Run individual test cases and the complete regression suite
- Document test scope, test approach, issues, and solutions

---

## 🌐 Application Under Test

**Website:** [Automation Exercise](https://automationexercise.com/)

Automation Exercise is an e-commerce demo website containing features such as:

- User registration
- User login/logout
- Product browsing
- Product search
- Product categories
- Product brands
- Shopping cart
- Checkout
- Payment
- Contact Us
- Subscription
- Product reviews
- Recommended products

---

# 🧪 Test Scope

## Automated Test Cases

The following test cases are automated:

| Test Case | Feature | Automation |
|-----------|---------|------------|
| TC_01 | Register User | ✅ Automated |
| TC_02 | Login User with correct credentials | ✅ Automated |
| TC_03 | Login User with incorrect credentials | ✅ Automated |
| TC_04 | Logout User | ✅ Automated |
| TC_05 | Register User with existing email | ✅ Automated |
| TC_06 | Contact Us Form | ✅ Automated |
| TC_07 | Verify Test Cases Page | ✅ Automated |
| TC_08 | Verify All Products and Product Detail Page | ✅ Automated |
| TC_09 | Search Product | ✅ Automated |
| TC_10 | Verify Subscription on Home Page | ✅ Automated |
| TC_11 | Verify Subscription in Cart | ✅ Automated |
| TC_12 | Add Products to Cart | ✅ Automated |
| TC_13 | Verify Product Quantity in Cart | ✅ Automated |
| TC_14 | Place Order - Register While Checkout | ✅ Automated |
| TC_15 | Place Order - Register Before Checkout | ✅ Automated |
| TC_16 | Place Order - Login Before Checkout | ✅ Automated |
| TC_17 | Remove Products from Cart | ✅ Automated |
| TC_18 | View Category Products | ✅ Automated |
| TC_19 | View Brand Products | ✅ Automated |
| TC_20 | Search Products and Verify Cart After Login | ✅ Automated |
| TC_21 | Add Product Review | ✅ Automated |
| TC_22 | Add Recommended Product to Cart | ✅ Automated |
| TC_23 | Verify Address in Checkout | ✅ Automated |
| TC_24 | Download Invoice | ❌ Manual Only |
| TC_25 | Scroll Down and Verify Bottom Text | ❌ Manual Only |
| TC_26 | Scroll Up and Verify Page | ❌ Manual Only |

### Automation Scope

- **23 automated test cases:** TC_01–TC_23
- **3 manual-only test cases:** TC_24–TC_26

TC_24–TC_26 were intentionally excluded from the automation scope for this project.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Programming language |
| Selenium WebDriver | Web UI automation |
| Pytest | Test framework |
| Google Chrome | Browser for test execution |
| Page Object Model | Test architecture/design pattern |
| JSON | Test data management |
| ConfigParser | Configuration management |
| Git | Version control |
| GitHub | Source code repository |
| VS Code | Development environment |

---

# 🏗️ Framework Architecture

The project follows the **Page Object Model (POM)** design pattern.

The framework separates:

- Test logic
- Page locators
- Page actions
- Configuration
- Test data
- Driver management
- Utility functions

### Test Flow

```text
Test Case
    ↓
Page Object
    ↓
Base Page
    ↓
Selenium WebDriver
    ↓
Automation Exercise Website
```

---

# 📁 Project Structure

```text
automation-exercise-pom/
│
├── .venv/
│
├── config/
│   └── config.ini
│
├── data/
│   ├── test_data.json
│   └── files/
│       └── contact_test.txt
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── contact_us_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── payment_page.py
│   └── signup_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_contact_us.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_other_features.py
│   ├── test_products.py
│   ├── test_register.py
│   └── test_subscription.py
│
├── utils/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── driver_factory.py
│   ├── screenshot.py
│   └── test_data_reader.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📂 Folder Responsibilities

## `pages/`

Contains Page Object classes.

Each Page Object contains:

- Page locators
- Page actions
- Page-specific verification methods

Examples:

```text
HomePage
LoginPage
SignupPage
ProductsPage
CartPage
CheckoutPage
PaymentPage
ContactUsPage
```

---

## `tests/`

Contains Pytest automated test cases.

The test files are organized by feature:

```text
test_register.py
test_login.py
test_logout.py
test_products.py
test_cart.py
test_checkout.py
test_contact_us.py
test_subscription.py
test_other_features.py
```

Each test file contains automated scenarios related to a specific application feature.

---

## `utils/`

Contains reusable framework utilities.

### `driver_factory.py`

Responsible for creating and configuring the Selenium WebDriver.

### `config_reader.py`

Reads configuration from:

```text
config/config.ini
```

### `test_data_reader.py`

Reads test data from:

```text
data/test_data.json
```

### `screenshot.py`

Provides screenshot-related utility functions.

---

## `data/`

Stores external test data.

Example:

```text
data/test_data.json
```

The test data contains information required by registration and login scenarios.

---

## `config/`

Contains framework configuration.

Example:

```ini
[DEFAULT]
base_url = https://automationexercise.com
browser = chrome
timeout = 10
```

---

# ⚙️ Prerequisites

Before running the project, make sure the following are installed:

### 1. Python

Python 3.14 or another compatible Python 3.x version.

Verify the installation:

```bash
python --version
```

Example:

```text
Python 3.14.7
```

### 2. Google Chrome

Install Google Chrome on the machine.

### 3. Git

Verify Git:

```bash
git --version
```

### 4. VS Code

VS Code is recommended as the development environment.

---

# 🚀 Clone and Run the Project

Follow these steps to run the project on a new Windows machine.

---

## Step 1 - Clone the Repository

Open PowerShell or Command Prompt:

```bash
git clone https://github.com/thuhuyen126/automation-exercise-pom.git
```

Move into the project directory:

```bash
cd automation-exercise-pom
```

---

## Step 2 - Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

---

## Step 3 - Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

After activation, the terminal should show:

```text
(.venv)
```

For example:

```text
(.venv) PS D:\automation-exercise-pom>
```

---

## Step 4 - Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Main dependencies:

```text
selenium
pytest
```

---

## Step 5 - Verify the Environment

Check Python:

```bash
python --version
```

Check Selenium:

```bash
pip show selenium
```

Check Pytest:

```bash
pytest --version
```

---

# ▶️ Running the Tests

## Run All Automated Tests

Run the complete automation suite:

```bash
pytest -v -s
```

Expected result:

```text
23 passed
0 failed
0 error
```

---

## Run a Specific Test File

Example:

```bash
pytest tests/test_login.py -v -s
```

---

## Run a Specific Test Case

Example:

```bash
pytest tests/test_login.py::test_tc03_invalid_login -v -s
```

---

## View Collected Tests

To check which tests Pytest discovers:

```bash
pytest --collect-only -q
```

Expected:

```text
23 tests collected
```

---

# 🧪 Example Test Case

## TC_03 - Login User with Incorrect Credentials

The manual test case is converted into automation through the following process:

```text
Manual Test Case
       ↓
Identify UI Elements
       ↓
Find Stable Locators
       ↓
Create/Update Page Object
       ↓
Implement Test Steps
       ↓
Add Assertions
       ↓
Execute Test
       ↓
Analyze Result
```

Example:

```python
def test_tc03_invalid_login(driver):
    home_page = HomePage(driver)

    home_page.click_signup_login()

    login_page = LoginPage(driver)

    login_page.login(
        "invalid@example.com",
        "invalid_password"
    )

    assert login_page.is_login_error_displayed()
```

The test verifies that the expected error message is displayed when invalid login credentials are submitted.

---

# 🔄 Manual Test Case to Automation Process

The automation process used in this project follows these steps:

## Step 1 - Understand the Manual Test Case

Example:

```text
TC_03 - Login User with incorrect email and password
```

Manual steps:

```text
1. Click Signup / Login
2. Enter incorrect email
3. Enter incorrect password
4. Click Login
5. Verify error message
```

---

## Step 2 - Identify UI Elements

Identify the elements that need to be automated:

```text
Signup/Login link
Email input
Password input
Login button
Error message
```

---

## Step 3 - Find Locators

Use Chrome Developer Tools to identify stable locators.

Possible locator strategies:

```text
ID
Name
CSS Selector
XPath
```

---

## Step 4 - Implement the Page Object

Put the locators and reusable actions inside the appropriate Page Object.

For TC_03:

```text
LoginPage
```

The Page Object handles:

- Enter username
- Enter password
- Click login
- Verify login error

---

## Step 5 - Create the Automated Test

The test file focuses on the business scenario rather than low-level Selenium operations.

Example:

```text
test_tc03_invalid_login()
```

---

## Step 6 - Add Assertions

Assertions verify whether the actual result matches the expected result.

Example:

```python
assert login_page.is_login_error_displayed()
```

---

## Step 7 - Execute and Debug

Run the test:

```bash
pytest -v -s
```

If the test fails:

```text
Check locator
     ↓
Check page state
     ↓
Check synchronization/wait
     ↓
Check test data
     ↓
Fix the issue
     ↓
Run again
```

---

# 🧩 Page Object Model

The framework uses Page Object Model to improve maintainability and reduce duplicated Selenium code.

Example architecture:

```text
tests/test_login.py
        ↓
LoginPage
        ↓
BasePage
        ↓
Selenium WebDriver
```

Instead of repeating Selenium operations in every test:

```python
driver.find_element(...)
driver.find_element(...)
driver.find_element(...)
```

Reusable methods are implemented in Page Objects:

```python
login_page.login(email, password)
```

This makes the test cases easier to read and maintain.

---

# 🧰 Test Data Management

Test data is stored separately from the test logic.

Example:

```text
data/test_data.json
```

This helps avoid hard-coding test data directly into test cases.

For user registration, the framework generates a unique email address during execution.

Example:

```python
email = f"automation_{uuid.uuid4().hex[:8]}@example.com"
```

This prevents repeated test executions from failing because the email address already exists.

---

# ⏱️ Synchronization and Wait Strategy

The framework uses Selenium explicit waits through `WebDriverWait`.

Explicit waits are used for conditions such as:

- Element presence
- Element visibility
- Element clickability
- URL changes
- JavaScript alerts

This helps reduce timing-related failures caused by asynchronous page loading.

---

# ⚠️ Known Issues and Solutions

During development and execution, several issues were encountered and resolved.

## 1. Google Vignette / Advertisement Interference

### Problem

Google advertisement/vignette pages occasionally appeared and interfered with navigation.

### Solution

The framework detects Google Vignette URLs and attempts to recover navigation.

---

## 2. Selenium Page Load Timeout

### Problem

Some pages could take longer than the configured page load timeout.

### Solution

A page-load timeout strategy was implemented so the test could continue when appropriate.

---

## 3. JavaScript Alert Handling

### Problem

TC_06 displays a JavaScript alert after submitting the Contact Us form.

### Solution

The test explicitly waits for the alert and accepts it.

Example:

```python
alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

alert.accept()
```

---

## 4. Duplicate Registration Email

### Problem

The website does not allow registration with an existing email address.

### Solution

TC_01 generates a unique email address for every execution.

---

## 5. Individual Test vs Full Suite Execution

Some issues appeared differently when running an individual test compared with running the complete test suite.

### Solution

Tests were executed both individually and as a complete regression suite to verify stability.

---

# 📊 Test Execution Result

The final automation suite was executed successfully.

| Result | Count |
|--------|------:|
| Total Automated Tests | 23 |
| Passed | 23 |
| Failed | 0 |
| Errors | 0 |
| Pass Rate | 100% |

### Final Result

```text
================ test session starts ================

collected 23 items

23 passed

================ 23 passed in 312.96s ================
```

**23/23 automated test cases passed successfully.**

---

# 📋 Testing Approach

The project uses a combination of manual testing and automation testing.

## Functional Testing

The main functional areas include:

- User registration
- User login
- User logout
- Product search
- Product details
- Shopping cart
- Checkout
- Contact Us
- Subscription
- Product categories
- Product brands
- Product reviews
- Recommended products
- Address verification

---

## Equivalence Partitioning

Equivalence Partitioning was considered when dividing input data into valid and invalid groups.

Example:

```text
Login Email

Valid email
Invalid email
Empty email
```

---

## Boundary Value Analysis

Boundary Value Analysis was considered for inputs where boundary conditions are relevant.

Example:

```text
Product quantity

Minimum valid quantity
Typical quantity
Higher quantity
Invalid quantity
```

---

## Manual + Automation Testing

The project follows:

```text
Manual Testing
      +
Automation Testing
```

Manual testing was used to understand and verify the scenarios.

Stable, repetitive, and regression-friendly scenarios were then automated using Selenium and Pytest.

---

# 🎯 Why These Test Cases Were Automated

Good automation candidates generally have the following characteristics:

- Frequently executed
- Repetitive
- Stable
- Rule-based
- Time-consuming when executed manually
- Important for regression testing
- Have clear expected results

Examples in this project include:

```text
Login
Registration
Product Search
Shopping Cart
Checkout
Subscription
Product Review
```

---

# 📌 Test Execution Strategy

## Individual Test

Useful during development and debugging:

```bash
pytest tests/test_login.py -v -s
```

## Full Regression Suite

Useful after changes:

```bash
pytest -v -s
```

The full regression suite verifies that existing functionality remains stable after framework or test changes.

---

# 🔐 Test Data and Configuration

The project keeps configuration and test data outside the main test logic.

### Configuration

```text
config/config.ini
```

Contains:

```text
Base URL
Browser
Timeout
```

### Test Data

```text
data/test_data.json
```

Contains data required by the automated tests.

---

# 🧹 Git and GitHub

Git is used for source code version control.

The project repository is hosted on GitHub:

**Repository:**

https://github.com/thuhuyen126/automation-exercise-pom

Basic Git workflow:

```bash
git status

git add .

git commit -m "Update automation framework"

git push
```

---

# 🚫 Files Excluded from Git

The following files and folders are excluded through `.gitignore`:

```text
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.coverage
htmlcov/
.vscode/
.idea/
.DS_Store
Thumbs.db
*.log
.env
```

This prevents unnecessary local and environment-specific files from being committed to the repository.

---

# 📈 Future Improvements

Possible future improvements include:

- Add cross-browser testing
- Add parameterized testing
- Improve test data management
- Add HTML test reports
- Add Allure reporting
- Improve screenshot capture on test failure
- Add CI/CD using GitHub Actions
- Add parallel test execution
- Improve logging
- Add API testing
- Add mobile automation using Appium
- Add Playwright automation for comparison

---

# 🎓 Skills Demonstrated

## Manual Testing

- Test case design
- Functional testing
- Test execution
- Test checklist creation
- Test planning
- Bug identification
- Regression testing
- Test analysis

## Automation Testing

- Selenium WebDriver
- Python
- Pytest
- Page Object Model
- Explicit Wait
- XPath / CSS / ID locators
- Test data management
- Configuration management
- Assertions
- JavaScript alert handling
- File upload automation
- Dynamic test data
- Test suite execution

## Tools

- VS Code
- Git
- GitHub
- Chrome DevTools

---

# 👩‍💻 Author

**Vu Thi Thu Huyen**

Software Engineering Graduate  
Aspiring QA Automation Tester

### Technologies

```text
Python
Selenium
Pytest
Manual Testing
Automation Testing
Git
GitHub
```

---

# ⭐ Project Summary

This project demonstrates the process of converting manual functional test cases into a maintainable Selenium automation framework.

The final implementation successfully automates:

```text
TC_01 → TC_23
```

Final execution result:

```text
23 Passed
0 Failed
0 Error
100% Pass Rate
```

TC_24–TC_26 remain **manual test cases** and are intentionally excluded from the automation scope.

---

## 📎 Repository

https://github.com/thuhuyen126/automation-exercise-pom
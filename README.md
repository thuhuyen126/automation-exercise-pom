# Automation Exercise - Selenium Pytest Automation

Automated testing framework for [Automation Exercise](https://automationexercise.com/) built with **Python, Selenium WebDriver, Pytest and Page Object Model (POM)**.

The project automates **23 test cases (TC_01 - TC_23)** covering user registration, authentication, products, cart, checkout, subscription, contact form, product reviews and other core e-commerce functionalities.

---

## 📌 Project Overview

This project was developed to practice and demonstrate UI automation testing using Selenium WebDriver with Python.

### Main objectives

- Automate functional test cases for an e-commerce website.
- Apply the **Page Object Model (POM)** design pattern.
- Separate test logic, page objects, test data and configuration.
- Create reusable Selenium utility methods.
- Handle dynamic test data such as unique email addresses.
- Use Pytest fixtures for WebDriver and test-user management.
- Verify expected UI results using assertions.
- Build a maintainable automation test structure.

---

## 🛠️ Technologies & Tools

| Technology / Tool | Purpose |
|---|---|
| Python 3.14.7 | Programming language |
| Selenium 4.48.0 | Browser automation |
| Pytest 9.1.1 | Test framework |
| Google Chrome | Test browser |
| Page Object Model | Test automation design pattern |
| JSON | Test data management |
| INI | Configuration management |
| VS Code | Development environment |

---

## 📂 Project Structure

```text
automation_exercise_pom/
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
│   ├── product_detail_page.py
│   ├── products_page.py
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
└── README.md
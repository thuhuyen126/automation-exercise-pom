import pytest
import uuid

from selenium.common.exceptions import TimeoutException

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.test_data_reader import TestDataReader
from utils.config_reader import ConfigReader
from utils.driver_factory import DriverFactory


@pytest.fixture
def driver():
    config = ConfigReader()

    browser = config.get("browser")
    base_url = config.get("base_url")

    driver = DriverFactory.create_driver(browser)

    try:
        driver.get(base_url)

    except TimeoutException:
        print(
            "\n[WARNING] Page load timeout. "
            "Trying to continue with the current page..."
        )

        try:
            driver.execute_script(
                "window.stop();"
            )
        except Exception:
            pass

    yield driver

    driver.quit()


@pytest.fixture
def registered_user(driver):
    data = TestDataReader().data["register_user"]

    email = f"automation_{uuid.uuid4().hex[:8]}@example.com"

    # ==========================================
    # REGISTER USER
    # ==========================================

    home_page = HomePage(driver)
    home_page.click_signup_login()

    login_page = LoginPage(driver)

    login_page.signup(
        data["name"],
        email
    )

    signup_page = SignupPage(driver)

    assert signup_page.is_account_information_displayed()

    signup_page.select_title_mr()
    signup_page.enter_password(data["password"])

    signup_page.select_date_of_birth(
        data["day"],
        data["month"],
        data["year"]
    )

    signup_page.select_newsletter()
    signup_page.select_special_offers()

    signup_page.enter_address_information(
        data["first_name"],
        data["last_name"],
        data["company"],
        data["address"],
        data["address_2"],
        data["state"],
        data["city"],
        data["zipcode"],
        data["mobile_number"]
    )

    signup_page.select_country(data["country"])

    signup_page.click_create_account()

    assert signup_page.is_account_created()

    signup_page.click_continue()

    # ==========================================
    # MAKE SURE USER IS LOGGED IN
    # ==========================================

    driver.get("https://automationexercise.com")

    home_page = HomePage(driver)

    if not home_page.is_logged_in():

        home_page.click_signup_login()

        login_page = LoginPage(driver)

        login_page.login(
            email,
            data["password"]
        )

        assert home_page.is_logged_in()

    # ==========================================
    # LOGOUT BEFORE TEST
    # ==========================================

    home_page.click_logout()

    yield {
        "email": email,
        "password": data["password"],
        "name": data["name"]
    }

    # =========================================================
    # CLEANUP
    # =========================================================

    try:

        driver.get("https://automationexercise.com")

        home_page = HomePage(driver)

        # Login again if necessary
        if not home_page.is_logged_in():

            home_page.click_signup_login()

            login_page = LoginPage(driver)

            login_page.login(
                email,
                data["password"]
            )

        # Delete account
        if home_page.is_logged_in():

            home_page.click_delete_account()

            signup_page = SignupPage(driver)

            if signup_page.is_account_deleted():

                signup_page.click_continue()

    except Exception as e:

        print(
            f"\n[WARNING] Account cleanup failed: {e}"
        )
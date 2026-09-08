import pytest
import uuid

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
    driver.get(base_url)

    yield driver

    driver.quit()


@pytest.fixture
def registered_user(driver):
    data = TestDataReader().data["register_user"]

    email = f"automation_{uuid.uuid4().hex[:8]}@example.com"

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

    assert home_page.is_logged_in()

    # Logout before the test starts
    home_page.click_logout()

    yield {
        "email": email,
        "password": data["password"],
        "name": data["name"]
    }

    # Cleanup
    # Login again before deleting the account
    home_page.click_signup_login()

    login_page = LoginPage(driver)

    login_page.login(
        email,
        data["password"]
    )

    assert home_page.is_logged_in()

    home_page.click_delete_account()

    assert signup_page.is_account_deleted()

    signup_page.click_continue()

def test_tc02_login_user(driver, registered_user):
    home_page = HomePage(driver)

    home_page.click_signup_login()

    login_page = LoginPage(driver)

    assert login_page.is_login_page_displayed()

    login_page.login(
        registered_user["email"],
        registered_user["password"]
    )

    assert home_page.is_logged_in()

    home_page.click_logout()

def test_tc03_login_with_incorrect_credentials(driver):
    home_page = HomePage(driver)

    home_page.click_signup_login()

    login_page = LoginPage(driver)

    assert login_page.is_login_page_displayed()

    login_page.login(
        "invalid_user@example.com",
        "WrongPassword123"
    )

    assert login_page.is_login_error_displayed()
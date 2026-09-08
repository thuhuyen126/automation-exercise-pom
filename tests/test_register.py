import uuid

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.test_data_reader import TestDataReader


def test_tc01_register_user(driver):
    # Read test data
    data = TestDataReader().data["register_user"]

    # Generate unique email
    email = f"automation_{uuid.uuid4().hex[:8]}@example.com"

    # Step 1: Home page
    home_page = HomePage(driver)

    # Step 2: Click Signup / Login
    home_page.click_signup_login()

    # Step 3: Signup section
    login_page = LoginPage(driver)

    assert login_page.is_signup_section_displayed()

    login_page.signup(
        data["name"],
        email
    )

    # Step 4: Account Information
    signup_page = SignupPage(driver)

    assert signup_page.is_account_information_displayed()

    # Step 5: Fill account information
    signup_page.select_title_mr()
    signup_page.enter_password(data["password"])

    signup_page.select_date_of_birth(
        data["day"],
        data["month"],
        data["year"]
    )

    signup_page.select_newsletter()
    signup_page.select_special_offers()

    # Step 6: Fill address information
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

    # Step 7: Create account
    signup_page.click_create_account()

    # Step 8: Verify account created
    assert signup_page.is_account_created()

    # Step 9: Continue
    signup_page.click_continue()

    # Step 10: Verify logged in
    assert home_page.is_logged_in()

    # Step 11: Delete account
    home_page.click_delete_account()

    # Step 12: Verify account deleted
    assert signup_page.is_account_deleted()

    # Step 13: Continue
    signup_page.click_continue()


def test_tc05_register_with_existing_email(driver, registered_user):
    home_page = HomePage(driver)

    home_page.click_signup_login()

    login_page = LoginPage(driver)

    assert login_page.is_signup_section_displayed()

    login_page.signup(
        registered_user["name"],
        registered_user["email"]
    )

    assert login_page.is_signup_error_displayed()
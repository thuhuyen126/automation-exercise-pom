from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_tc04_logout_user(driver, registered_user):
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

    assert login_page.is_login_page_displayed()
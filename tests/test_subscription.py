from pages.home_page import HomePage


def test_tc10_verify_subscription_home_page(driver):
    home_page = HomePage(driver)

    # Scroll down to the bottom of the Home page
    home_page.scroll_to_subscription()

    # Verify SUBSCRIPTION is displayed
    assert home_page.is_subscription_displayed()

    # Enter email and subscribe
    home_page.subscribe("automation_subscription@example.com")

    # Verify successful subscription message
    assert home_page.is_subscription_success_displayed()


def test_tc11_verify_subscription_cart_page(driver):
    home_page = HomePage(driver)

    # Open Cart page
    home_page.click_cart()

    # Scroll down to the bottom of the Cart page
    home_page.scroll_to_subscription()

    # Verify SUBSCRIPTION is displayed
    assert home_page.is_subscription_displayed()

    # Enter email and subscribe
    home_page.subscribe("automation_cart_subscription@example.com")

    # Verify successful subscription message
    assert home_page.is_subscription_success_displayed()
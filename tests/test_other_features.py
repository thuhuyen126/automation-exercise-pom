from pages.home_page import HomePage


def test_tc07_verify_test_cases_page(driver):

    home_page = HomePage(driver)

    # Click Test Cases
    home_page.click_test_cases()

    # Verify Test Cases page
    assert "test_cases" in driver.current_url
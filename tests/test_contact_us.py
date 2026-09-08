from pathlib import Path

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from utils.test_data_reader import TestDataReader


def test_tc06_contact_us_form(driver):

    # Read test data
    data = TestDataReader().data["contact_us"]

    # Open Contact Us
    home_page = HomePage(driver)
    home_page.click_contact_us()

    contact_page = ContactUsPage(driver)

    # Verify Contact Us page
    assert contact_page.is_get_in_touch_displayed()

    # Fill Contact Us form
    contact_page.enter_name(data["name"])
    contact_page.enter_email(data["email"])
    contact_page.enter_subject(data["subject"])
    contact_page.enter_message(data["message"])

    # Upload file
    file_path = (
        Path(__file__).parent.parent
        / "data"
        / "files"
        / "contact_test.txt"
    )

    contact_page.upload_file(str(file_path.resolve()))

    # Submit form
    contact_page.click_submit()

    # Wait for confirmation alert
    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    print(f"\n[INFO] Alert text: {alert.text}")

    alert.accept()

    # Verify success message
    assert contact_page.is_success_message_displayed()

    # Go Home
    contact_page.click_home()
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactUsPage(BasePage):

    GET_IN_TOUCH_TITLE = (
        By.XPATH,
        "//h2[contains(., 'Get In Touch')]"
    )

    NAME_INPUT = (
        By.CSS_SELECTOR,
        "input[data-qa='name']"
    )

    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "input[data-qa='email']"
    )

    SUBJECT_INPUT = (
        By.CSS_SELECTOR,
        "input[data-qa='subject']"
    )

    MESSAGE_INPUT = (
        By.CSS_SELECTOR,
        "textarea[data-qa='message']"
    )

    UPLOAD_FILE = (
        By.CSS_SELECTOR,
        "input[type='file']"
    )

    SUBMIT_BUTTON = (
        By.CSS_SELECTOR,
        "input[data-qa='submit-button']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(), 'Success! Your details have been submitted successfully.')]"
    )

    HOME_BUTTON = (
        By.XPATH,
        "//a[contains(., 'Home')]"
    )

    def is_get_in_touch_displayed(self):
        return self.is_visible(self.GET_IN_TOUCH_TITLE)

    def enter_name(self, name):
        self.type_text(self.NAME_INPUT, name)

    def enter_email(self, email):
        self.type_text(self.EMAIL_INPUT, email)

    def enter_subject(self, subject):
        self.type_text(self.SUBJECT_INPUT, subject)

    def enter_message(self, message):
        self.type_text(self.MESSAGE_INPUT, message)

    def upload_file(self, file_path):
        self.find_element(self.UPLOAD_FILE).send_keys(file_path)

    def click_submit(self):
        button = self.find_element(self.SUBMIT_BUTTON)

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def is_success_message_displayed(self):
        return self.is_visible(self.SUCCESS_MESSAGE)

    def click_home(self):
        self.click(self.HOME_BUTTON)
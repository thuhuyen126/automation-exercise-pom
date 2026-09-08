from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_TO_ACCOUNT_TITLE = (
        By.XPATH,
        "//h2[contains(., 'Login to your account')]"
    )

    NEW_USER_SIGNUP_TITLE = (
        By.XPATH,
        "//h2[contains(., 'New User Signup!')]"
    )

    LOGIN_EMAIL = (
        By.CSS_SELECTOR,
        "input[data-qa='login-email']"
    )

    LOGIN_PASSWORD = (
        By.CSS_SELECTOR,
        "input[data-qa='login-password']"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-qa='login-button']"
    )

    SIGNUP_NAME = (
        By.CSS_SELECTOR,
        "input[data-qa='signup-name']"
    )

    SIGNUP_EMAIL = (
        By.CSS_SELECTOR,
        "input[data-qa='signup-email']"
    )

    SIGNUP_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-qa='signup-button']"
    )

    LOGIN_ERROR = (
        By.XPATH,
        "//p[contains(., 'Your email or password is incorrect!')]"
    )

    SIGNUP_ERROR = (
        By.XPATH,
        "//p[contains(., 'Email Address already exist!')]"
    )

    def is_login_page_displayed(self):
        return self.is_visible(self.LOGIN_TO_ACCOUNT_TITLE)

    def is_signup_section_displayed(self):
        return self.is_visible(self.NEW_USER_SIGNUP_TITLE)

    def login(self, email, password):
        self.type_text(self.LOGIN_EMAIL, email)
        self.type_text(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def signup(self, name, email):
        self.type_text(self.SIGNUP_NAME, name)
        self.type_text(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)

    def is_login_error_displayed(self):
        return self.is_visible(self.LOGIN_ERROR)

    def is_signup_error_displayed(self):
        return self.is_visible(self.SIGNUP_ERROR)
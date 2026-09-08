from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):

    ACCOUNT_INFORMATION_TITLE = (
        By.XPATH,
        "//b[contains(., 'Enter Account Information')]"
    )

    TITLE_MR = (
        By.ID,
        "id_gender1"
    )

    TITLE_MRS = (
        By.ID,
        "id_gender2"
    )

    PASSWORD = (
        By.ID,
        "password"
    )

    DAY = (
        By.ID,
        "days"
    )

    MONTH = (
        By.ID,
        "months"
    )

    YEAR = (
        By.ID,
        "years"
    )

    NEWSLETTER_CHECKBOX = (
        By.ID,
        "newsletter"
    )

    OFFERS_CHECKBOX = (
        By.ID,
        "optin"
    )

    FIRST_NAME = (
        By.ID,
        "first_name"
    )

    LAST_NAME = (
        By.ID,
        "last_name"
    )

    COMPANY = (
        By.ID,
        "company"
    )

    ADDRESS = (
        By.ID,
        "address1"
    )

    ADDRESS_2 = (
        By.ID,
        "address2"
    )

    COUNTRY = (
        By.ID,
        "country"
    )

    STATE = (
        By.ID,
        "state"
    )

    CITY = (
        By.ID,
        "city"
    )

    ZIPCODE = (
        By.ID,
        "zipcode"
    )

    MOBILE_NUMBER = (
        By.ID,
        "mobile_number"
    )

    CREATE_ACCOUNT_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-qa='create-account']"
    )

    ACCOUNT_CREATED_TITLE = (
        By.XPATH,
        "//b[contains(., 'Account Created!')]"
    )

    CONTINUE_BUTTON = (
        By.CSS_SELECTOR,
        "a[data-qa='continue-button']"
    )

    ACCOUNT_DELETED_TITLE = (
        By.XPATH,
        "//b[contains(., 'Account Deleted!')]"
    )

    def is_account_information_displayed(self):
        return self.is_visible(self.ACCOUNT_INFORMATION_TITLE)

    def select_title_mr(self):
        self.click(self.TITLE_MR)

    def select_title_mrs(self):
        self.click(self.TITLE_MRS)

    def enter_password(self, password):
        self.type_text(self.PASSWORD, password)

    def select_date_of_birth(self, day, month, year):
        from selenium.webdriver.support.ui import Select

        Select(self.find_element(self.DAY)).select_by_value(str(day))
        Select(self.find_element(self.MONTH)).select_by_value(str(month))
        Select(self.find_element(self.YEAR)).select_by_value(str(year))

    def select_newsletter(self):
        element = self.find_element(self.NEWSLETTER_CHECKBOX)

        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
    )

        self.driver.execute_script(
        "arguments[0].click();",
        element
    )

    def select_special_offers(self):
        element = self.find_element(self.OFFERS_CHECKBOX)

        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
    )

        self.driver.execute_script(
        "arguments[0].click();",
        element
    )

    def enter_address_information(
        self,
        first_name,
        last_name,
        company,
        address,
        address_2,
        state,
        city,
        zipcode,
        mobile_number
    ):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.COMPANY, company)
        self.type_text(self.ADDRESS, address)
        self.type_text(self.ADDRESS_2, address_2)
        self.type_text(self.STATE, state)
        self.type_text(self.CITY, city)
        self.type_text(self.ZIPCODE, zipcode)
        self.type_text(self.MOBILE_NUMBER, mobile_number)

    def select_country(self, country):
        from selenium.webdriver.support.ui import Select

        Select(self.find_element(self.COUNTRY)).select_by_visible_text(country)

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created(self):
        return self.is_visible(self.ACCOUNT_CREATED_TITLE)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def is_account_deleted(self):
        return self.is_visible(self.ACCOUNT_DELETED_TITLE)

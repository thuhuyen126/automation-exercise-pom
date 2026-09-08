from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    SIGNUP_LOGIN_LINK = (
        By.XPATH,
        "//a[contains(., 'Signup / Login')]"
    )

    CONTACT_US_LINK = (
        By.XPATH,
        "//a[contains(., 'Contact us')]"
    )

    PRODUCTS_LINK = (
        By.XPATH,
        "//a[contains(., 'Products')]"
    )

    CART_LINK = (
        By.XPATH,
        "//a[contains(., 'Cart')]"
    )

    TEST_CASES_LINK = (
        By.XPATH,
        "//a[contains(., 'Test Cases')]"
    )

    LOGGED_IN_AS = (
        By.XPATH,
        "//a[contains(., 'Logged in as')]"
    )

    DELETE_ACCOUNT_LINK = (
        By.XPATH,
        "//a[contains(., 'Delete Account')]"
    )

    LOGOUT_LINK = (
    By.XPATH,
    "//a[contains(., 'Logout')]"
    )

    SUBSCRIPTION_TITLE = (
        By.XPATH,
        "//h2[contains(., 'Subscription')]"
    )

    SUBSCRIPTION_EMAIL = (
        By.ID,
        "susbscribe_email"
    )

    SUBSCRIBE_BUTTON = (
        By.ID,
        "subscribe"
    )

    SUBSCRIPTION_SUCCESS = (
        By.XPATH,
        "//*[contains(., 'You have been successfully subscribed!')]"
    )

        # TC_22 - Recommended Items
    RECOMMENDED_ITEMS_TITLE = (
        By.XPATH,
        "//h2[contains(., 'recommended items') or contains(., 'Recommended Items')]"
    )

    RECOMMENDED_FIRST_PRODUCT = (
        By.XPATH,
        "(//div[@id='recommended-item-carousel']//div[contains(@class, 'item')])[1]"
    )

    RECOMMENDED_FIRST_ADD_TO_CART = (
        By.XPATH,
        "(//div[@id='recommended-item-carousel']//div[contains(@class, 'item')])[1]"
        "//a[contains(@class, 'add-to-cart')]"
    )

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    def click_contact_us(self):
        self.click(self.CONTACT_US_LINK)

    def click_products(self):
        self.click(self.PRODUCTS_LINK)

    def click_cart(self):
        self.click(self.CART_LINK)

    def click_test_cases(self):
        self.click(self.TEST_CASES_LINK)

    def is_logged_in(self):
        return self.is_visible(self.LOGGED_IN_AS)

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def scroll_to_subscription(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            self.find_element(self.SUBSCRIPTION_TITLE)
        )

    def is_subscription_displayed(self):
        return self.is_visible(self.SUBSCRIPTION_TITLE)

    def subscribe(self, email):
        self.type_text(self.SUBSCRIPTION_EMAIL, email)
        self.click(self.SUBSCRIBE_BUTTON)

    def is_subscription_success_displayed(self):
        return self.is_visible(self.SUBSCRIPTION_SUCCESS)

    def is_recommended_items_displayed(self):
        return self.is_visible(self.RECOMMENDED_ITEMS_TITLE)

    def scroll_to_recommended_items(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            self.find_element(self.RECOMMENDED_ITEMS_TITLE)
        )

    def add_first_recommended_product_to_cart(self):
        element = self.find_element(self.RECOMMENDED_FIRST_ADD_TO_CART)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )
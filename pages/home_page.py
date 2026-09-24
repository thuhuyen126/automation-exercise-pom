from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    # =========================
    # Navigation
    # =========================

    SIGNUP_LOGIN_LINK = (
        By.CSS_SELECTOR,
        "a[href='/login']"
    )

    CONTACT_US_LINK = (
        By.CSS_SELECTOR,
        "a[href='/contact_us']"
    )

    PRODUCTS_LINK = (
        By.CSS_SELECTOR,
        "a[href='/products']"
    )

    CART_LINK = (
        By.CSS_SELECTOR,
        "a[href='/view_cart']"
    )

    TEST_CASES_LINK = (
        By.CSS_SELECTOR,
        "a[href='/test_cases']"
    )

    LOGGED_IN_AS = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Logged in as')]"
    )

    DELETE_ACCOUNT_LINK = (
        By.CSS_SELECTOR,
        "a[href='/delete_account']"
    )

    LOGOUT_LINK = (
        By.CSS_SELECTOR,
        "a[href='/logout']"
    )

    # =========================
    # Subscription
    # =========================

    SUBSCRIPTION_TITLE = (
        By.XPATH,
        "//h2[normalize-space()='Subscription']"
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
        "//*[contains(normalize-space(), "
        "'You have been successfully subscribed!')]"
    )

    # =========================
    # Recommended Items - TC_22
    # =========================

    RECOMMENDED_ITEMS_TITLE = (
        By.XPATH,
        "//h2[normalize-space()='recommended items' "
        "or normalize-space()='Recommended Items']"
    )

    RECOMMENDED_FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "#recommended-item-carousel .item"
    )

    RECOMMENDED_FIRST_ADD_TO_CART = (
        By.CSS_SELECTOR,
        "#recommended-item-carousel .item:first-child "
        "a.add-to-cart"
    )

    # =========================
    # Navigation Actions
    # =========================

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

    # =========================
    # Account
    # =========================

    def is_logged_in(self):
        return self.is_visible(self.LOGGED_IN_AS)

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK)

    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    # =========================
    # Subscription
    # =========================

    def scroll_to_subscription(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            self.find_element(self.SUBSCRIPTION_TITLE)
        )

    def is_subscription_displayed(self):
        return self.is_visible(self.SUBSCRIPTION_TITLE)

    def subscribe(self, email):
        self.type_text(self.SUBSCRIPTION_EMAIL, email)
        self.click(self.SUBSCRIBE_BUTTON)

    def is_subscription_success_displayed(self):
        return self.is_visible(self.SUBSCRIPTION_SUCCESS)

    # =========================
    # Recommended Items - TC_22
    # =========================

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
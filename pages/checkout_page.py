from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    REGISTER_LOGIN_LINK = (
        By.XPATH,
        "//p[contains(., 'Register / Login')]//a"
    )

    ADDRESS_DETAILS_TITLE = (
        By.XPATH,
        "//h2[contains(., 'Address Details')]"
    )

    REVIEW_ORDER_TITLE = (
        By.XPATH,
        "//h2[contains(., 'Review Your Order')]"
    )

    ORDER_COMMENT = (
        By.NAME,
        "message"
    )

    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//a[contains(., 'Place Order')]"
    )

    DELIVERY_ADDRESS = (
        By.ID,
        "address_delivery"
    )

    BILLING_ADDRESS = (
        By.ID,
        "address_invoice"
    )

    def click_register_login(self):
        self.click(self.REGISTER_LOGIN_LINK)

    def is_address_details_displayed(self):
        return self.is_visible(self.ADDRESS_DETAILS_TITLE)

    def is_review_order_displayed(self):
        return self.is_visible(self.REVIEW_ORDER_TITLE)

    def enter_order_comment(self, comment):
        self.type_text(self.ORDER_COMMENT, comment)

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def is_delivery_address_displayed(self):
        return self.is_visible(self.DELIVERY_ADDRESS)

    def is_billing_address_displayed(self):
        return self.is_visible(self.BILLING_ADDRESS)
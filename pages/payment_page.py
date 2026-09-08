from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PaymentPage(BasePage):

    NAME_ON_CARD = (
        By.CSS_SELECTOR,
        "input[data-qa='name-on-card']"
    )

    CARD_NUMBER = (
        By.CSS_SELECTOR,
        "input[data-qa='card-number']"
    )

    CVC = (
        By.CSS_SELECTOR,
        "input[data-qa='cvc']"
    )

    EXPIRY_MONTH = (
        By.CSS_SELECTOR,
        "input[data-qa='expiry-month']"
    )

    EXPIRY_YEAR = (
        By.CSS_SELECTOR,
        "input[data-qa='expiry-year']"
    )

    PAY_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-qa='pay-button']"
    )

    ORDER_SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(., 'Order Placed!')]"
    )

    def enter_payment_information(
        self,
        name_on_card,
        card_number,
        cvc,
        expiry_month,
        expiry_year
    ):
        self.type_text(self.NAME_ON_CARD, name_on_card)
        self.type_text(self.CARD_NUMBER, card_number)
        self.type_text(self.CVC, cvc)
        self.type_text(self.EXPIRY_MONTH, expiry_month)
        self.type_text(self.EXPIRY_YEAR, expiry_year)

    def click_pay_and_confirm(self):
        self.click(self.PAY_BUTTON)

    def is_order_success_displayed(self):
        return self.is_visible(self.ORDER_SUCCESS_MESSAGE)
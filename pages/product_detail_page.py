from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductDetailPage(BasePage):

    PRODUCT_INFORMATION = (
        By.XPATH,
        "//div[contains(@class, 'product-information')]"
    )

    PRODUCT_NAME = (
        By.XPATH,
        "//div[contains(@class, 'product-information')]//h2"
    )

    CATEGORY = (
        By.XPATH,
        "//div[contains(@class, 'product-information')]//p[contains(., 'Category:')]"
    )

    PRICE = (
        By.XPATH,
        "//div[contains(@class, 'product-information')]//span[contains(., 'Rs.')]"
    )

    AVAILABILITY = (
        By.XPATH,
        "//div[contains(@class, 'product-information')]//p[contains(., 'Availability:')]"
    )

    CONDITION = (
        By.XPATH,
        "//div[contains(@class, 'product-information')]//p[contains(., 'Condition:')]"
    )

    BRAND = (
        By.XPATH,
        "//div[contains(@class, 'product-information')]//p[contains(., 'Brand:')]"
    )

    QUANTITY_INPUT = (
    By.ID,
    "quantity"
    )

    ADD_TO_CART_BUTTON = (
    By.XPATH,
    "//button[contains(., 'Add to cart')]"
    )

        # =========================
    # TC_21 - Add Product Review
    # =========================

    REVIEW_NAME = (
        By.ID,
        "name"
    )

    REVIEW_EMAIL = (
        By.ID,
        "email"
    )

    REVIEW_TEXT = (
        By.ID,
        "review"
    )

    REVIEW_SUBMIT_BUTTON = (
        By.ID,
        "button-review"
    )

    REVIEW_SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class, 'alert-success')]"
        "//span[contains(., 'Thank you for your review.')]"
    )

    def is_product_information_displayed(self):
        return (
            self.is_product_name_displayed()
            and self.is_category_displayed()
            and self.is_price_displayed()
            and self.is_availability_displayed()
            and self.is_condition_displayed()
            and self.is_brand_displayed()
    )

    def is_product_name_displayed(self):
        return self.is_visible(self.PRODUCT_NAME)

    def is_category_displayed(self):
        return self.is_visible(self.CATEGORY)

    def is_price_displayed(self):
        return self.is_visible(self.PRICE)

    def is_availability_displayed(self):
        return self.is_visible(self.AVAILABILITY)

    def is_condition_displayed(self):
        return self.is_visible(self.CONDITION)

    def is_brand_displayed(self):
        return self.is_visible(self.BRAND)

    def set_quantity(self, quantity):
        self.type_text(self.QUANTITY_INPUT, str(quantity))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def enter_review_name(self, name):
        self.type_text(self.REVIEW_NAME, name)

    def enter_review_email(self, email):
        self.type_text(self.REVIEW_EMAIL, email)

    def enter_review(self, review):
        self.type_text(self.REVIEW_TEXT, review)

    def submit_review(self):
        self.click(self.REVIEW_SUBMIT_BUTTON)

    def is_review_success_displayed(self):
        return self.is_visible(self.REVIEW_SUCCESS_MESSAGE)
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    CART_PRODUCTS = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr"
    )

    PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr[id^='product-']"
    )

    PRODUCT_PRICES = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr[id^='product-'] .cart_price p"
    )

    PRODUCT_QUANTITIES = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr[id^='product-'] .cart_quantity button"
    )

    PRODUCT_TOTALS = (
        By.CSS_SELECTOR,
        "#cart_info_table tbody tr[id^='product-'] .cart_total p"
    )

    PROCEED_TO_CHECKOUT_BUTTON = (
        By.XPATH,
        "//a[contains(., 'Proceed To Checkout')]"
    )

    REMOVE_FIRST_PRODUCT = (
        By.XPATH,
        "(//a[contains(@class, 'cart_quantity_delete')])[1]"
    )

    def get_product_count(self):
        return len(
            self.driver.find_elements(*self.PRODUCT_NAMES)
        )

    def are_products_displayed(self):
        return self.is_visible(self.CART_PRODUCTS)

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [element.text for element in elements]

    def get_product_quantities(self):
        elements = self.driver.find_elements(*self.PRODUCT_QUANTITIES)
        return [element.text for element in elements]

    def get_product_totals(self):
        elements = self.driver.find_elements(*self.PRODUCT_TOTALS)
        return [element.text for element in elements]

    def get_first_product_quantity(self):
        quantities = self.driver.find_elements(*self.PRODUCT_QUANTITIES)
        return quantities[0].text

    def click_proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def remove_first_product(self):
        self.click(self.REMOVE_FIRST_PRODUCT)

    def wait_for_cart_empty(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.PRODUCT_NAMES)
            ) == 0
        )

    def is_product_in_cart(self, product_name):
        product_names = self.get_product_names()

        return any(
            product_name.lower() in name.lower()
            for name in product_names
        )    
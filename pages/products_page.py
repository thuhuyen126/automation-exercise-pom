from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):

    ALL_PRODUCTS_TITLE = (
        By.XPATH,
        "//h2[contains(., 'All Products')]"
    )

    FIRST_PRODUCT = (
        By.XPATH,
        "(//div[contains(@class, 'product-image-wrapper')])[1]"
    )

    FIRST_PRODUCT_NAME = (
        By.XPATH,
        "(//div[contains(@class, 'productinfo')]//p)[1]"
    )

    FIRST_PRODUCT_VIEW_BUTTON = (
        By.XPATH,
        "(//a[contains(., 'View Product')])[1]"
    )

    SEARCH_INPUT = (
        By.ID,
        "search_product"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    SEARCHED_PRODUCTS_TITLE = (
        By.XPATH,
        "//h2[contains(., 'Searched Products')]"
    )

    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//div[contains(@class, 'product-image-wrapper')]"
    )

    FIRST_PRODUCT_ADD_TO_CART = (
        By.XPATH,
        "(//div[contains(@class, 'product-image-wrapper')])[1]"
        "//a[contains(@class, 'add-to-cart')]"
    )

    SECOND_PRODUCT_ADD_TO_CART = (
        By.XPATH,
        "(//div[contains(@class, 'product-image-wrapper')])[2]"
        "//a[contains(@class, 'add-to-cart')]"
    )

    CONTINUE_SHOPPING_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Continue Shopping')]"
    )

    VIEW_CART_BUTTON = (
        By.XPATH,
        "//u[contains(., 'View Cart')]"
    )

    # =========================
    # TC_18 - Category Products
    # =========================

    WOMEN_CATEGORY = (
        By.XPATH,
        "//div[@id='accordian']//a[@href='#Women']"
    )

    DRESS_CATEGORY = (
        By.XPATH,
        "//div[@id='Women']//a[contains(normalize-space(), 'Dress')]"
    )

    CATEGORY_PRODUCTS_TITLE = (
        By.XPATH,
        "//h2[contains(translate(., "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), "
        "'dress products')]"
    )

    # =========================
    # TC_19 - Brand Products
    # =========================

    POLO_BRAND = (
        By.XPATH,
        "//div[@class='brands_products']//a[contains(., 'Polo')]"
    )

    HM_BRAND = (
        By.XPATH,
        "//div[@class='brands_products']//a[contains(., 'H&M')]"
    )

    BRAND_PRODUCTS_TITLE = (
        By.XPATH,
        "//h2[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'products')]"
    )

    def search_product(self, product_name):
        self.type_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def is_searched_products_displayed(self):
        return self.is_visible(self.SEARCHED_PRODUCTS_TITLE)

    def are_searched_products_displayed(self):
        return self.is_visible(self.SEARCHED_PRODUCTS)

    def is_all_products_displayed(self):
        return self.is_visible(self.ALL_PRODUCTS_TITLE)

    def is_first_product_displayed(self):
        return self.is_visible(self.FIRST_PRODUCT)

    def get_first_product_name(self):
        return self.get_text(self.FIRST_PRODUCT_NAME)

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT_VIEW_BUTTON)

    def add_first_product_to_cart(self):
        self.click(self.FIRST_PRODUCT_ADD_TO_CART)

    def add_second_product_to_cart(self):
        self.click(self.SECOND_PRODUCT_ADD_TO_CART)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def click_view_cart(self):
        self.click(self.VIEW_CART_BUTTON)

    # =========================
    # TC_18 methods
    # =========================

    def click_women_category(self):
        dress_elements = self.driver.find_elements(*self.DRESS_CATEGORY)

        # Nếu Women đã mở thì không click nữa
        if dress_elements and dress_elements[0].is_displayed():
            return

        # Nếu đang đóng thì click Women để mở
        self.click(self.WOMEN_CATEGORY)

        self.wait.until(
            EC.visibility_of_element_located(self.DRESS_CATEGORY)
        )

    def click_dress_category(self):
        self.click(self.DRESS_CATEGORY)

    def is_category_products_displayed(self):
        return self.is_visible(self.CATEGORY_PRODUCTS_TITLE)

    def click_polo_brand(self):
        self.click(self.POLO_BRAND)


    def click_hm_brand(self):
        self.click(self.HM_BRAND)


    def is_polo_products_displayed(self):
        locator = (
            By.XPATH,
            "//h2[contains(translate(., "
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
            "'abcdefghijklmnopqrstuvwxyz'), "
            "'polo products')]"
        )

        return self.is_visible(locator)


    def is_hm_products_displayed(self):
        locator = (
            By.XPATH,
            "//h2[contains(translate(., "
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
            "'abcdefghijklmnopqrstuvwxyz'), "
            "'h&m products')]"
        )

        return self.is_visible(locator)
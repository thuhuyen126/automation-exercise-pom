from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_tc08_verify_product_detail(driver):
    # Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    products_page = ProductsPage(driver)

    # Verify All Products page is displayed
    assert products_page.is_all_products_displayed()

    # Verify first product is displayed
    assert products_page.is_first_product_displayed()

    # Get first product name
    first_product_name = products_page.get_first_product_name()
    assert first_product_name

    # Click View Product of first product
    products_page.click_first_product()

    # Verify product detail page
    product_detail_page = ProductDetailPage(driver)

    assert product_detail_page.is_product_information_displayed()
    assert product_detail_page.is_product_name_displayed()
    assert product_detail_page.is_category_displayed()
    assert product_detail_page.is_price_displayed()
    assert product_detail_page.is_availability_displayed()
    assert product_detail_page.is_condition_displayed()
    assert product_detail_page.is_brand_displayed()

def test_tc09_search_product(driver):
    # Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    products_page = ProductsPage(driver)

    # Verify All Products page is displayed
    assert products_page.is_all_products_displayed()

    # Search for a product
    products_page.search_product("Blue Top")

    # Verify SEARCHED PRODUCTS is displayed
    assert products_page.is_searched_products_displayed()

    # Verify searched products are displayed
    assert products_page.are_searched_products_displayed()

def test_tc18_view_category_products(driver):
    home_page = HomePage(driver)
    home_page.click_products()

    print("\nCURRENT URL:", driver.current_url)
    print("PAGE TITLE:", driver.title)

    products_page = ProductsPage(driver, timeout=20)

    print(
        "ALL PRODUCTS DISPLAYED:",
        products_page.is_all_products_displayed()
    )

    assert products_page.is_all_products_displayed()

def test_tc19_view_brand_products(driver):
    home_page = HomePage(driver)
    home_page.click_products()

    products_page = ProductsPage(driver)

    assert products_page.is_all_products_displayed()

    # Select Polo brand
    products_page.click_polo_brand()

    assert products_page.is_polo_products_displayed()

    # Select H&M brand
    products_page.click_hm_brand()

    assert products_page.is_hm_products_displayed()

def test_tc20_search_product_cart_login_verify_cart(driver, registered_user):
    # 1. Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    products_page = ProductsPage(driver)

    # 2. Verify All Products page
    assert products_page.is_all_products_displayed()

    # 3. Search for a product
    product_name = "Blue Top"
    products_page.search_product(product_name)

    # 4. Verify searched products are displayed
    assert products_page.is_searched_products_displayed()
    assert products_page.are_searched_products_displayed()

    # 5. Add searched product to cart
    products_page.add_first_product_to_cart()

    # 6. View Cart
    products_page.click_view_cart()

    cart_page = CartPage(driver)

    # 7. Verify product is in Cart
    assert cart_page.is_product_in_cart(product_name)

    # 8. Go to Login page
    home_page = HomePage(driver)
    home_page.click_signup_login()

    login_page = LoginPage(driver)

    # 9. Verify Login page
    assert login_page.is_login_page_displayed()

    # 10. Login with registered user
    login_page.login(
        registered_user["email"],
        registered_user["password"]
    )

    # 11. Verify user is logged in
    assert home_page.is_logged_in()

    # 12. Open Cart again
    home_page.click_cart()

    # 13. Verify product is still in Cart after login
    cart_page = CartPage(driver)

    assert cart_page.is_product_in_cart(product_name)

def test_tc21_add_product_review(driver):
    # 1. Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    products_page = ProductsPage(driver)

    # 2. Verify All Products page
    assert products_page.is_all_products_displayed()

    # 3. Open first product
    products_page.click_first_product()

    product_detail_page = ProductDetailPage(driver)

    # 4. Enter review information
    product_detail_page.enter_review_name("Automation Tester")
    product_detail_page.enter_review_email("automation@test.com")
    product_detail_page.enter_review(
        "This product is good and easy to use."
    )

    # 5. Submit review
    product_detail_page.submit_review()

    # 6. Verify review success message
    assert product_detail_page.is_review_success_displayed()

def test_tc22_add_recommended_item_to_cart(driver):
    # 1. Verify Home page
    home_page = HomePage(driver)

    # 2. Scroll to Recommended Items
    home_page.scroll_to_recommended_items()

    # 3. Verify Recommended Items is displayed
    assert home_page.is_recommended_items_displayed()

    # 4. Add first recommended product to cart
    home_page.add_first_recommended_product_to_cart()

    # 5. Click View Cart from popup
    products_page = ProductsPage(driver)
    products_page.click_view_cart()

    # 6. Verify product is displayed in Cart
    cart_page = CartPage(driver)
    assert cart_page.are_products_displayed()
import uuid

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.payment_page import PaymentPage
from utils.test_data_reader import TestDataReader
from pages.login_page import LoginPage


def test_tc14_place_order_register_while_checkout(driver):

    data = TestDataReader().data["register_user"]

    # Create unique email
    email = f"automation_{uuid.uuid4().hex[:8]}@example.com"

    # Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    # Add first product to cart
    products_page = ProductsPage(driver)

    assert products_page.is_all_products_displayed()

    products_page.add_first_product_to_cart()

    # View Cart
    products_page.click_view_cart()

    # Proceed to Checkout
    cart_page = CartPage(driver)
    cart_page.click_proceed_to_checkout()

    # Click Register / Login
    checkout_page = CheckoutPage(driver)
    checkout_page.click_register_login()

    # Register new user
    login_page = LoginPage(driver)
    login_page.signup(data["name"], email)

    # Verify Account Information page
    signup_page = SignupPage(driver)
    assert signup_page.is_account_information_displayed()

    # Fill account information
    signup_page.select_title_mr()
    signup_page.enter_password(data["password"])
    signup_page.select_date_of_birth(
        data["day"],
        data["month"],
        data["year"]
    )

    signup_page.select_newsletter()
    signup_page.select_special_offers()

    signup_page.enter_address_information(
        data["first_name"],
        data["last_name"],
        data["company"],
        data["address"],
        data["address_2"],
        data["state"],
        data["city"],
        data["zipcode"],
        data["mobile_number"]
    )

    signup_page.select_country(data["country"])

    # Create account
    signup_page.click_create_account()

    assert signup_page.is_account_created()

    # Continue after account creation
    signup_page.click_continue()

    # Verify user is logged in
    assert home_page.is_logged_in()

    # Go to Cart
    home_page.click_cart()

    # Proceed to Checkout again
    cart_page = CartPage(driver)
    cart_page.click_proceed_to_checkout()

    # Verify address and order review
    checkout_page = CheckoutPage(driver)

    assert checkout_page.is_address_details_displayed()
    assert checkout_page.is_review_order_displayed()

    # Enter order comment
    checkout_page.enter_order_comment(
        "Test order for TC_14"
    )

    # Place order
    checkout_page.click_place_order()

    # Enter payment information
    payment_page = PaymentPage(driver)

    payment_page.enter_payment_information(
        "Automation Test",
        "4111111111111111",
        "123",
        "12",
        "2030"
    )

    # Pay and confirm order
    payment_page.click_pay_and_confirm()

    # Verify order placed successfully
    assert payment_page.is_order_success_displayed()

def test_tc15_place_order_register_before_checkout(driver, registered_user):

    # Login with registered user
    home_page = HomePage(driver)
    home_page.click_signup_login()

    login_page = LoginPage(driver)
    login_page.login(
        registered_user["email"],
        registered_user["password"]
    )

    assert home_page.is_logged_in()

    # Open Products page
    home_page.click_products()

    # Add first product to cart
    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()

    # View Cart
    products_page.click_view_cart()

    # Proceed to Checkout
    cart_page = CartPage(driver)
    cart_page.click_proceed_to_checkout()

    # Verify address and order review
    checkout_page = CheckoutPage(driver)

    assert checkout_page.is_address_details_displayed()
    assert checkout_page.is_review_order_displayed()

    # Enter order comment
    checkout_page.enter_order_comment(
        "Test order for TC_15"
    )

    # Place Order
    checkout_page.click_place_order()

    # Enter payment information
    payment_page = PaymentPage(driver)

    payment_page.enter_payment_information(
        "Automation Test",
        "4111111111111111",
        "123",
        "12",
        "2030"
    )

    # Pay and confirm
    payment_page.click_pay_and_confirm()

    # Verify order success
    assert payment_page.is_order_success_displayed()

def test_tc16_place_order_login_before_checkout(driver, registered_user):
    home_page = HomePage(driver)

    # Login with existing user
    home_page.click_signup_login()

    login_page = LoginPage(driver)

    login_page.login(
        registered_user["email"],
        registered_user["password"]
    )

    assert home_page.is_logged_in()

    # Go to Products
    home_page.click_products()

    products_page = ProductsPage(driver)

    # Add first product
    products_page.add_first_product_to_cart()

    # View cart
    products_page.click_view_cart()

    cart_page = CartPage(driver)

    # Proceed to checkout
    cart_page.click_proceed_to_checkout()

    checkout_page = CheckoutPage(driver)

    # Verify checkout page
    assert checkout_page.is_address_details_displayed()
    assert checkout_page.is_review_order_displayed()

    # Enter comment
    checkout_page.enter_order_comment(
        "Test order for TC_16"
    )

    # Place order
    checkout_page.click_place_order()

    # Payment
    payment_page = PaymentPage(driver)

    payment_page.enter_payment_information(
        "Automation Test",
        "4111111111111111",
        "123",
        "12",
        "2030"
    )

    payment_page.click_pay_and_confirm()

    # Verify order placed
    assert payment_page.is_order_success_displayed()

def test_tc23_verify_delivery_and_billing_address_after_registration(driver):

    data = TestDataReader().data["register_user"]

    # Create unique email
    email = f"automation_{uuid.uuid4().hex[:8]}@example.com"

    # 1. Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    # 2. Add first product to cart
    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()

    # 3. View Cart
    products_page.click_view_cart()

    # 4. Proceed to Checkout
    cart_page = CartPage(driver)
    cart_page.click_proceed_to_checkout()

    # 5. Click Register / Login
    checkout_page = CheckoutPage(driver)
    checkout_page.click_register_login()

    # 6. Register new user
    login_page = LoginPage(driver)
    login_page.signup(data["name"], email)

    # 7. Verify Account Information page
    signup_page = SignupPage(driver)
    assert signup_page.is_account_information_displayed()

    # 8. Fill account information
    signup_page.select_title_mr()
    signup_page.enter_password(data["password"])

    signup_page.select_date_of_birth(
        data["day"],
        data["month"],
        data["year"]
    )

    signup_page.select_newsletter()
    signup_page.select_special_offers()

    signup_page.enter_address_information(
        data["first_name"],
        data["last_name"],
        data["company"],
        data["address"],
        data["address_2"],
        data["state"],
        data["city"],
        data["zipcode"],
        data["mobile_number"]
    )

    signup_page.select_country(data["country"])

    # 9. Create account
    signup_page.click_create_account()

    assert signup_page.is_account_created()

    # 10. Continue after account creation
    signup_page.click_continue()

    # 11. Verify user is logged in
    assert home_page.is_logged_in()

    # 12. Open Cart
    home_page.click_cart()

    # 13. Proceed to Checkout
    cart_page = CartPage(driver)
    cart_page.click_proceed_to_checkout()

    # 14. Verify Checkout page
    checkout_page = CheckoutPage(driver)

    assert checkout_page.is_address_details_displayed()
    assert checkout_page.is_review_order_displayed()

    # 15. Verify Delivery Address
    assert checkout_page.is_delivery_address_displayed()

    # 16. Verify Billing Address
    assert checkout_page.is_billing_address_displayed()
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage


def test_tc12_add_products_to_cart(driver):
    # Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    products_page = ProductsPage(driver)

    # Add first product to cart
    products_page.add_first_product_to_cart()

    # Continue shopping
    products_page.click_continue_shopping()

    # Add second product to cart
    products_page.add_second_product_to_cart()

    # View Cart
    products_page.click_view_cart()

    cart_page = CartPage(driver)

    # Verify cart contains 2 products
    assert cart_page.get_product_count() == 2

    # Verify product information is displayed
    assert cart_page.are_products_displayed()

    assert len(cart_page.get_product_names()) == 2
    assert len(cart_page.get_product_prices()) == 2
    assert len(cart_page.get_product_quantities()) == 2
    assert len(cart_page.get_product_totals()) == 2

def test_tc13_verify_product_quantity_is_4(driver):
    # Open Products page
    home_page = HomePage(driver)
    home_page.click_products()

    # Open first product detail
    products_page = ProductsPage(driver)
    products_page.click_first_product()

    # Set quantity = 4
    product_detail_page = ProductDetailPage(driver)
    product_detail_page.set_quantity(4)

    # Add product to cart
    product_detail_page.add_to_cart()

    # View Cart
    products_page.click_view_cart()

    # Verify quantity is 4
    cart_page = CartPage(driver)

    assert cart_page.get_product_count() == 1
    assert cart_page.get_first_product_quantity() == "4"

def test_tc17_remove_product_from_cart(driver):
    home_page = HomePage(driver)

    home_page.click_products()

    products_page = ProductsPage(driver)

    products_page.add_first_product_to_cart()

    products_page.click_view_cart()

    cart_page = CartPage(driver)

    assert cart_page.get_product_count() == 1

    cart_page.remove_first_product()

    cart_page.wait_for_cart_empty()

    assert cart_page.get_product_count() == 0
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.ui
@pytest.mark.smoke
def test_add_product_to_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_inventory_page_displayed()

    product_name = "Sauce Labs Backpack"

    inventory_page.add_product_to_cart(product_name)
    inventory_page.open_cart()

    assert cart_page.is_product_in_cart(product_name)
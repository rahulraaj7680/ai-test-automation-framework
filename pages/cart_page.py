from selenium.webdriver.common.by import By

from utils.logger import get_logger
from utils.wait_utils import WaitUtils


class CartPage:

    CART_ITEM = "inventory_item_name"
    CHECKOUT_BUTTON = "checkout"

    logger = get_logger("CartPage")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def is_product_in_cart(self, product_name):
        self.logger.info(
            f"Checking cart for product: {product_name}"
        )

        products = self.driver.find_elements(
            By.CLASS_NAME,
            self.CART_ITEM
        )

        return any(
            product.text == product_name
            for product in products
        )

    def click_checkout(self):
        self.logger.info("Clicking checkout")

        checkout = self.wait.wait_for_clickable(
            By.ID,
            self.CHECKOUT_BUTTON
        )

        checkout.click()
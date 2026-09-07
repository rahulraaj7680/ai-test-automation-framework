from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import get_logger
from utils.wait_utils import WaitUtils


class InventoryPage:
    INVENTORY_CONTAINER = "inventory_container"
    SHOPPING_CART = "shopping_cart_link"
    PRODUCT_ITEMS = "inventory_item"
    PRODUCT_NAMES = "inventory_item_name"

    logger = get_logger("InventoryPage")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def is_inventory_page_displayed(self):
        self.logger.info("Checking inventory page")

        element = self.wait.wait_for_visible(
            By.ID,
            self.INVENTORY_CONTAINER
        )

        return element.is_displayed()

    def add_product_to_cart(self, product_name):
        self.logger.info(
            f"Adding product to cart: {product_name}"
        )

        self.wait.wait_for_visible(
            By.CLASS_NAME,
            self.PRODUCT_ITEMS
        )

        all_products = self.driver.find_elements(
            By.CLASS_NAME,
            self.PRODUCT_ITEMS
        )

        for product in all_products:
            name = product.find_element(
                By.CLASS_NAME,
                self.PRODUCT_NAMES
            ).text

            if name == product_name:
                button = product.find_element(
                    By.CSS_SELECTOR,
                    "button"
                )

                WebDriverWait(
                    self.driver,
                    10
                ).until(
                    lambda driver: button.is_enabled()
                )

                button.click()

                self.logger.info(
                    f"Product added: {product_name}"
                )

                return

        raise ValueError(
            f"Product not found: {product_name}"
        )

    def open_cart(self):
        self.logger.info("Opening shopping cart")

        cart = self.wait.wait_for_clickable(
            By.CLASS_NAME,
            self.SHOPPING_CART
        )

        cart.click()
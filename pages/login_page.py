from selenium.webdriver.common.by import By

from utils.logger import get_logger
from utils.wait_utils import WaitUtils


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = "user-name"
    PASSWORD = "password"
    LOGIN_BUTTON = "login-button"

    logger = get_logger("LoginPage")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def open(self):
        self.logger.info("Opening SauceDemo login page")
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.logger.info("Entering username")

        element = self.wait.wait_for_visible(
            By.ID,
            self.USERNAME
        )

        element.send_keys(username)

    def enter_password(self, password):
        self.logger.info("Entering password")

        element = self.wait.wait_for_visible(
            By.ID,
            self.PASSWORD
        )

        element.send_keys(password)

    def click_login(self):
        self.logger.info("Clicking login button")

        button = self.wait.wait_for_clickable(
            By.ID,
            self.LOGIN_BUTTON
        )

        button.click()

    def login(self, username, password):
        self.logger.info("Performing login")

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        self.logger.info("Reading login error message")

        error = self.wait.wait_for_visible(
            By.CSS_SELECTOR,
            "[data-test='error']"
        )

        return error.text
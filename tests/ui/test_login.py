import pytest

from pages.login_page import LoginPage

from utils.config_reader import (
    get_test_username,
    get_test_password,
)


@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_login(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        get_test_username(),
        get_test_password(),
    )

    assert "inventory" in driver.current_url
import csv
import os

import pytest

from pages.login_page import LoginPage


def load_login_data():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "login_data.csv"
    )

    with open(file_path, newline="") as file:
        return list(csv.DictReader(file))

@pytest.mark.ui
@pytest.mark.parametrize("test_data", load_login_data())
def test_login_data_driven(driver, test_data):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    if test_data["expected_result"] == "success":
        assert "inventory" in driver.current_url

    else:
        error_message = login_page.get_error_message()
        assert error_message != ""
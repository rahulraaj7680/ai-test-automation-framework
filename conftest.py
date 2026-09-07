import os
from datetime import datetime

import pytest
from selenium import webdriver

from api.api_client import APIClient


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            test_name = item.name.replace(
                "[", "_"
            ).replace("]", "")

            screenshot_path = os.path.join(
                "screenshots",
                f"{test_name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_path)

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )
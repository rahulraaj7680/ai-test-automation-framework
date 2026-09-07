import os

from dotenv import load_dotenv


load_dotenv()


def get_test_username():
    return os.getenv("TEST_USERNAME")


def get_test_password():
    return os.getenv("TEST_PASSWORD")


def get_gemini_api_key():
    return os.getenv("GEMINI_API_KEY")


def get_api_base_url():
    return os.getenv(
        "API_BASE_URL",
        "https://jsonplaceholder.typicode.com"
    )
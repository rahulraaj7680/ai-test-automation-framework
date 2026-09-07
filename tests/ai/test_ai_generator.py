import os

import pytest

from ai.test_generator import AITestGenerator


@pytest.mark.ai
def test_generate_login_test_cases():

    requirement = """
    The application has a login page.

    Users should be able to log in using valid credentials.
    Invalid credentials should display an error message.
    Empty username or password should not allow login.
    """

    generator = AITestGenerator()

    result = generator.generate_test_cases(
        requirement
    )

    assert result
    assert len(result) > 0

    output_directory = "ai/generated_tests"

    os.makedirs(
        output_directory,
        exist_ok=True
    )

    output_file = os.path.join(
        output_directory,
        "login_test_cases.txt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(result)

    print(
        f"\nAI test cases saved to: {output_file}"
    )
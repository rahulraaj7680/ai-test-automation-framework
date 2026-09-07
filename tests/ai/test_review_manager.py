import pytest

from ai.review_manager import ReviewManager


@pytest.mark.ai
def test_only_approved_cases_are_selected():

    review_file = (
        "ai/generated_tests/review_status.csv"
    )

    manager = ReviewManager(
        review_file
    )

    approved_cases = (
        manager.get_approved_test_cases()
    )

    assert approved_cases == [
        "TC01",
        "TC02",
        "TC03",
    ]
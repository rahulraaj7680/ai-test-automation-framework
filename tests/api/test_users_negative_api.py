import pytest

from utils.api_assertions import APIAssertions


@pytest.mark.api
def test_get_invalid_endpoint(api_client):

    response = api_client.get(
        "/invalid-endpoint"
    )

    APIAssertions.assert_status_code(
        response,
        404
    )


@pytest.mark.api
def test_get_nonexistent_user(api_client):

    response = api_client.get(
        "/users/9999"
    )

    APIAssertions.assert_status_code(
        response,
        404
    )


@pytest.mark.api
def test_update_nonexistent_user(api_client):

    user_data = {
        "name": "Unknown User",
        "username": "unknown",
        "email": "unknown@example.com"
    }

    response = api_client.put(
        "/users/9999",
        user_data
    )

    APIAssertions.assert_status_code(
        response,
        500
    )


@pytest.mark.api
def test_delete_nonexistent_user(api_client):

    response = api_client.delete(
        "/users/9999"
    )

    APIAssertions.assert_status_code(
        response,
        200
    )
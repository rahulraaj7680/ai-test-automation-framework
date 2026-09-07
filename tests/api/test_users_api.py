import pytest

from tests.api.schemas.user_schema import USER_SCHEMA
from utils.api_assertions import APIAssertions
from utils.api_test_data import load_api_users
from utils.schema_validator import SchemaValidator


@pytest.mark.api
def test_get_users(api_client):

    response = api_client.get("/users")

    APIAssertions.assert_status_code(
        response,
        200
    )

    APIAssertions.assert_response_is_list(
        response
    )

    users = response.json()

    assert len(users) > 0

    first_user = users[0]

    SchemaValidator.validate_data(
        first_user,
        USER_SCHEMA
    )

    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user


@pytest.mark.api
@pytest.mark.parametrize(
    "user_data",
    load_api_users()
)
def test_create_user(
    api_client,
    user_data
):

    response = api_client.post(
        "/users",
        user_data
    )

    APIAssertions.assert_status_code(
        response,
        201
    )

    APIAssertions.assert_response_is_dict(
        response
    )

    APIAssertions.assert_json_field_value(
        response,
        "name",
        user_data["name"]
    )

    APIAssertions.assert_json_field_value(
        response,
        "username",
        user_data["username"]
    )

    APIAssertions.assert_json_field_value(
        response,
        "email",
        user_data["email"]
    )


@pytest.mark.api
def test_update_user(api_client):

    user_data = {
        "name": "Rahul Updated",
        "username": "rahul_updated",
        "email": "rahul.updated@example.com"
    }

    response = api_client.put(
        "/users/1",
        user_data
    )

    APIAssertions.assert_status_code(
        response,
        200
    )

    APIAssertions.assert_response_is_dict(
        response
    )

    APIAssertions.assert_json_field_value(
        response,
        "name",
        "Rahul Updated"
    )

    APIAssertions.assert_json_field_value(
        response,
        "username",
        "rahul_updated"
    )

    APIAssertions.assert_json_field_value(
        response,
        "email",
        "rahul.updated@example.com"
    )


@pytest.mark.api
def test_delete_user(api_client):

    response = api_client.delete(
        "/users/1"
    )

    APIAssertions.assert_status_code(
        response,
        200
    )
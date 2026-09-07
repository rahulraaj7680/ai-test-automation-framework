class APIAssertions:

    @staticmethod
    def assert_status_code(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected status code {expected_status}, "
            f"but received {response.status_code}"
        )

    @staticmethod
    def assert_json_field(response, field):
        data = response.json()

        assert field in data, (
            f"Expected field '{field}' "
            f"not found in response"
        )

    @staticmethod
    def assert_json_field_value(
        response,
        field,
        expected_value
    ):
        data = response.json()

        assert field in data, (
            f"Expected field '{field}' "
            f"not found in response"
        )

        assert data[field] == expected_value, (
            f"Expected '{field}' to be "
            f"'{expected_value}', "
            f"but received '{data[field]}'"
        )

    @staticmethod
    def assert_response_is_list(response):
        data = response.json()

        assert isinstance(data, list), (
            "Expected response to be a list"
        )

    @staticmethod
    def assert_response_is_dict(response):
        data = response.json()

        assert isinstance(data, dict), (
            "Expected response to be a dictionary"
        )
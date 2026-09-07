from jsonschema import validate


class SchemaValidator:

    @staticmethod
    def validate_data(data, schema):
        validate(
            instance=data,
            schema=schema
        )

        return True

    @staticmethod
    def validate_response(response, schema):
        return SchemaValidator.validate_data(
            response.json(),
            schema
        )
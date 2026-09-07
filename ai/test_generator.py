from google import genai

from utils.config_reader import get_gemini_api_key


class AITestGenerator:

    def __init__(self):
        api_key = get_gemini_api_key()

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(api_key=api_key)

    def generate_test_cases(self, requirement):

        prompt = f"""
You are a senior QA automation engineer.

Analyze the following software requirement:

{requirement}

Generate comprehensive test cases covering:

1. Positive scenarios
2. Negative scenarios
3. Boundary cases
4. Edge cases
5. Security-related input cases

For every test case provide:

- Test Case ID
- Title
- Description
- Preconditions
- Test Steps
- Expected Result
- Priority

Do not generate automation code.

Return the test cases in a clear structured format.
"""

        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
        )

        return response.text
# AI-Assisted Test Automation Framework

A reusable test automation framework built with **Python, Selenium, PyTest, Requests, and Google Gemini** to automate UI workflows, REST API validation, data-driven testing, schema validation, and AI-assisted test-case generation.

The framework follows a modular architecture using the **Page Object Model (POM)** and reusable utilities, with **GitHub Actions CI/CD** for automated API test execution.

---

## 🚀 Features

- UI automation using Selenium WebDriver
- Test execution using PyTest
- Page Object Model (POM)
- REST API automation using Requests
- Positive and negative API testing
- Data-driven testing using CSV and JSON
- JSON Schema response validation
- Reusable API assertion utilities
- Explicit waits for Selenium synchronization
- Centralized configuration using `.env`
- Logging support
- Automatic screenshots on UI test failures
- HTML test reporting
- PyTest markers for selective execution
- AI-assisted test-case generation using Google Gemini
- Human review/approval workflow for AI-generated test cases
- Git version control
- GitHub Actions CI/CD

---

## 🏗️ Project Architecture

```text
ai-test-automation-framework/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── ai/
│   ├── generated_tests/
│   │   ├── login_test_cases.txt
│   │   └── review_status.csv
│   ├── review_manager.py
│   └── test_generator.py
│
├── api/
│   ├── __init__.py
│   └── api_client.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/
│   ├── ai/
│   │   ├── test_ai_generator.py
│   │   └── test_review_manager.py
│   │
│   ├── api/
│   │   ├── schemas/
│   │   │   └── user_schema.py
│   │   ├── test_users_api.py
│   │   └── test_users_negative_api.py
│   │
│   ├── data/
│   │   ├── api_users.json
│   │   └── login_data.csv
│   │
│   └── ui/
│       ├── test_login.py
│       ├── test_login_data_driven.py
│       └── test_products.py
│
├── utils/
│   ├── api_assertions.py
│   ├── api_test_data.py
│   ├── config_reader.py
│   ├── logger.py
│   ├── run_tests.py
│   ├── schema_validator.py
│   └── wait_utils.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

| Technology     | Purpose                     |
| -------------- | --------------------------- |
| Python         | Programming language        |
| PyTest         | Test framework              |
| Selenium       | UI automation               |
| Requests       | REST API automation         |
| JSON Schema    | API response validation     |
| Google Gemini  | AI-assisted test generation |
| python-dotenv  | Environment configuration   |
| pytest-html    | HTML test reports           |
| Git            | Version control             |
| GitHub Actions | CI/CD                       |


🌐 Applications Under Test
UI Testing

SauceDemo

https://www.saucedemo.com/

The UI suite validates important workflows such as:

Valid login
Invalid login
Empty credentials
Data-driven login scenarios
Product selection
Shopping cart validation


API Testing

JSONPlaceholder

https://jsonplaceholder.typicode.com

The API suite validates:

GET users
POST users
PUT users
DELETE users
Invalid endpoints
Non-existent users
Response data types
Required JSON fields
JSON Schema validation

AI-Assisted Test Generation

The framework integrates Google Gemini to generate structured test cases from software requirements.

The AI generator considers:

Positive scenarios
Negative scenarios
Boundary cases
Edge cases
Security-related input cases

The AI does not directly add generated cases into the automation suite.

Instead, generated test cases go through a manual review process.
Software Requirement
        ↓
Google Gemini
        ↓
AI-Generated Test Cases
        ↓
Human Review
        ↓
APPROVED / PENDING / REJECTED
        ↓
Approved Test Cases
        ↓
Automation Suite

Configuration

Create a .env file in the project root:

TEST_USERNAME=standard_user
TEST_PASSWORD=secret_sauce
GEMINI_API_KEY=your_gemini_api_key
API_BASE_URL=https://jsonplaceholder.typicode.com

Never commit .env to Git.

The repository provides .env.example as a template.

Installation
1. Clone the repository
git clone https://github.com/rahulraaj7680/ai-test-automation-framework.git
cd ai-test-automation-framework
2. Create a virtual environment
python3 -m venv venv
3. Activate the virtual environment
macOS / Linux
source venv/bin/activate
Windows
venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Configure environment variables

Create .env:

cp .env.example .env

Then update the values inside .env.

🧪 Running Tests
Run the complete test suite
pytest -v
Run API tests
pytest -m api -v
Run UI tests
pytest -m ui -v
Run smoke tests
pytest -m smoke -v
Run UI smoke tests
pytest -m "ui and smoke" -v
Run AI tests
pytest -m ai -v
📊 HTML Test Report

The framework includes HTML reporting through pytest-html.

Generate a report using:

python utils/run_tests.py

The report is generated at:

reports/test_report.html

You can also execute a specific marker:

python utils/run_tests.py api

or:

python utils/run_tests.py "ui and smoke"
📸 Failure Screenshots

When a Selenium UI test fails, the framework automatically captures a screenshot.

Screenshots are stored in:

screenshots/

Example:

screenshots/
└── test_saucedemo_login_20260907_120000.png

This makes UI failures easier to investigate.

📝 Logging

The framework uses centralized logging utilities.

Logs are stored in:

logs/

The API and UI layers log important execution events such as:

Page navigation
User actions
API requests
API response status codes
Test execution events
🔌 API Framework Design

The API layer uses a reusable APIClient.

Instead of implementing HTTP request logic separately inside every test, the framework centralizes request handling:

Test
 ↓
APIAssertions
 ↓
APIClient
 ↓
Requests
 ↓
REST API

Supported operations:

GET
POST
PUT
DELETE

The client also provides:

Centralized timeout configuration
Common HTTP headers
Query parameter support
Request logging
Response status logging
📐 API Schema Validation

API responses are validated against JSON Schemas.

Example:

API Response
     ↓
JSON Schema
     ↓
Schema Validator
     ↓
Pass / Fail

This allows the framework to validate not only HTTP status codes but also the structure and data types of API responses.

📚 Data-Driven Testing

Test data is separated from test logic.

UI

Login scenarios are stored in:

tests/data/login_data.csv
API

User test data is stored in:

tests/data/api_users.json

PyTest parameterization executes the same test logic against multiple datasets.

🧩 Page Object Model

The UI framework follows the Page Object Model.

Example:

LoginPage
    ↓
login()
    ↓
InventoryPage
    ↓
add_product_to_cart()
    ↓
CartPage

Page-specific locators and actions are kept inside page classes rather than directly inside test cases.

This improves:

Maintainability
Reusability
Readability
Scalability
🔄 CI/CD

The project uses GitHub Actions to automatically execute API tests.

Workflow:

Developer Push
      ↓
GitHub Repository
      ↓
GitHub Actions
      ↓
Install Python
      ↓
Install Dependencies
      ↓
Run API Tests
      ↓
Pass / Fail

Workflow configuration:

.github/workflows/tests.yml

The CI pipeline runs API tests on:

Push to main
Pull requests targeting main
🧪 Test Coverage

The current framework includes automated coverage for:

UI
Login success
Login failure
Invalid credentials
Empty username
Data-driven login scenarios
Product selection
Cart validation
API
GET users
POST users
PUT users
DELETE users
Invalid endpoints
Non-existent resources
Response structure
JSON Schema validation
Data-driven API requests
AI
AI test-case generation
Review status management
Approved / pending / rejected test cases
🛡️ Secure Coding Practices

The framework follows basic secure automation practices:

Secrets are stored in environment variables
.env is excluded through .gitignore
.env.example contains only placeholder values
API keys are not hard-coded
AI-generated test cases are manually reviewed before acceptance
📈 Future Improvements

Potential future enhancements include:

Cross-browser UI execution
Parallel test execution
Allure reporting
API authentication testing
More comprehensive security testing
Docker-based test execution
Test result notifications
Expanded AI-generated test-case approval workflow
CI execution for UI tests
👨‍💻 Author

Rahul Raj

GitHub:

https://github.com/rahulraaj7680

⭐ Project Highlights

This project demonstrates practical experience with:

Test Automation + API Testing + UI Testing + PyTest + Selenium + Data-Driven Testing + JSON Schema Validation + AI-Assisted Testing + Human Review + Git + CI/CD


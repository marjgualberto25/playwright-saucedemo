# Playwright SauceDemo Test Automation

Automated UI test suite for the [SauceDemo](https://www.saucedemo.com/) e-commerce practice site, built with **Playwright** and **pytest** in Python.

This is a personal portfolio project to apply my QA and business analysis experience to test automation, covering positive, negative, and edge-case scenarios.

## Tech Stack

- Python 3
- Playwright (pytest-playwright)
- pytest
- Git and GitHub

## Test Coverage

| ID | Scenario | Type | Expected Result |
|----|----------|------|-----------------|
| TC-01 | Login with valid credentials | Positive | User lands on the Products page |
| TC-02 | Login with invalid password | Negative | Error: credentials do not match |
| TC-03 | Login with locked-out user | Negative | Error: user is locked out |
| TC-04 | Login with empty username | Validation | Error: username is required |

## Project Structure

```
playwright-saucedemo/
├── tests/
│   └── test_login.py
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository and go into the folder
2. Create and activate a virtual environment:
```
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies:
```
   pip install pytest-playwright
   playwright install
```
4. Run the tests:
```
   pytest
```
   To watch the tests run in a browser:
```
   pytest --headed --slowmo 500
```

## Roadmap

- [x] Login tests (positive, negative, validation)
- [ ] Cart and checkout flow tests
- [ ] Page Object Model structure
- [ ] Data-driven tests from external test data
- [ ] HTML reports and screenshots on failure
- [ ] CI with GitHub Actions

## Author

**Marijoy Gualberto**, Business Analyst / QA Analyst with 7+ years in financial services and insurance
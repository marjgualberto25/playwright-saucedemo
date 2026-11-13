from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"

def login(page: Page, username: str, password: str):
    page.goto(URL)
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")

def test_valid_login(page: Page):
    login(page, "standard_user", "secret_sauce")
    expect(page.locator(".title")).to_have_text("Products")

def test_invalid_password(page: Page):
    login(page, "standard_user", "wrong_password")
    expect(page.locator("[data-test='error']")).to_contain_text("do not match")

def test_locked_out_user(page: Page):
    login(page, "locked_out_user", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")

def test_empty_username(page: Page):
    login(page, "", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("Username is required")
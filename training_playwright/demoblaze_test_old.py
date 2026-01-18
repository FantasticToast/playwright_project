from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.demoblaze.com/")
    login_button = page.locator("[id='login2']")
    login_button.click()
    username_input = page.locator("[id='loginusername']")
    username_input.fill("admin")
    password_input = page.locator("[id='loginpassword']")
    password_input.fill("admin")
    confirm_login_button = page.get_by_role("button", name="Log in")
    confirm_login_button.click()
    print(page.url)
    current_url = page.url
    assert current_url == "https://www.demoblaze.coms/", "unexpected url"

    page.close()
    browser.close()
    print("### Test end ###")
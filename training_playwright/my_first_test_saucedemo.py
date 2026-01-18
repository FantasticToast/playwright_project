from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("#user-name")
    user.fill("standard_user")
    password = page.locator("#password")
    password.type("secret_sauce")
    login_button = page.locator("#login-button")
    # login_button = page.get_by_text("login")
    login_button.click()
    current_url= page.url
    page.close()
    browser.close()
    print("### Test end ###", current_url)
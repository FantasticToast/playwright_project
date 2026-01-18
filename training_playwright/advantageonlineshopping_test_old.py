from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com")
    contact_button = page.get_by_role("link", name="CONTACT US")
    print(contact_button.inner_text())
    contact_button.click()

    print(page.url)

    page.close()
    browser.close()
    print("### Test end ###")
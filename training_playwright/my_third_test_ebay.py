from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")
    search = page.locator("[id='gh-ac']")
    search.fill("shirt")
    search_button = page.locator("[id='gh-search-btn']")
    search_button.click()
    # page.keyboard.press("Enter")
    text = search_button.inner_text()
    print(text)



    page.close()
    browser.close()
    print("### Test end ###")
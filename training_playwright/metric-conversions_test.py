from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.metric-conversions.org/")
    # area_conversion_button = page.get_by_title("Area Conversion")
    # print(area_conversion_button.inner_text())

    # print(page.url)

    page.close()
    browser.close()
    print("### Test end ###")
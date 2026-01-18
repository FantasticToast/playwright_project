from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net")
    bmi_button = page.get_by_role("link", name="BMI calculator")

    bmi_button.click()
    time.sleep(3)
    bmr_button = page.get_by_role("link", name="BMR")
    bmr_button.click()

    print(page.url)

    page.close()
    browser.close()
    print("### Test end ###")
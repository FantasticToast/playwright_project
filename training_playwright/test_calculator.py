class TestCalculator:

    def test_calculator_list(self,setup_playwright):
        print ("into test_calculator_list")
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        calculator_list = page.query_selector_all("a")
        for calculator in calculator_list:
            calculator_text = calculator.inner_text()
            print (calculator_text)
    def test_interest_drop_down(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.calculator.net/")
        interest = page.locator('[href="/interest-calculator.html"]')
        interest.click()
        dropdown = page.locator("#ccompound")
        dropdown.select_option("weekly")
        # dropdown.select_option(index = 4)
        # radio = page.locator("#cadditionat2")
        # radio = page.get_by_role("checkbox", name="end")
        # radio.click()
        print("end")


class TestDemoblaze:

    def test_demoblaze_correct_login(self, setup_playwright):
        print ("into test_demoblaze_correct_login")
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")
        login_button = page.locator("#login2")
        login_button.click()
        username_input = page.locator("#loginusername")
        username_input.fill("admin")
        password_input = page.locator("#loginpassword")
        password_input.fill("admin")
        confirm_login_button = page.get_by_role("button", name="Log in")
        confirm_login_button.click()
        current_url = page.url
        assert current_url == "https://www.demoblaze.com/", "unexpected url"

    def test_demoblaze_cart_button(self, setup_playwright):
        print ("into test_demoblaze_cart_button")
        page = setup_playwright
        page.goto("https://www.demoblaze.com/")
        cart_button = page.locator("#cartur")
        cart_button.click()
        current_url = page.url
        assert current_url == "https://www.demoblaze.com/cart.html", "unexpected url"
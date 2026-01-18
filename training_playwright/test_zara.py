class TestZara:

    def test_shopping_basket_is_zero(self, setup_playwright):
        print("into test_shopping_basket_is_zero")
        page = setup_playwright
        page.goto("https://www.zara.com/il/en/")
        shopping_basket_button = page.locator('[href="https://www.zara.com/il/en/shop/cart"]')
        basket_text = shopping_basket_button.inner_text()
        assert basket_text == str(basket_text)
        basket_text = basket_text.replace("SHOPPING BAG", "")
        basket_text = basket_text.replace("[", "")
        basket_text = basket_text.replace("]", "")
        assert int(basket_text) < 1
        print("end")
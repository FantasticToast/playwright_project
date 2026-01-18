class TestAdvantageOnlineShopping:

    def test_contact_us_fill_and_send(self, setup_playwright):
        print("into test_contact_us_fill_and_send")
        page = setup_playwright
        page.goto("https://advantageonlineshopping.com/#/")
        contact_us_button = page.get_by_role("Link",  name="CONTACT US")
        contact_us_button.click()
        dropdown_select_category = page.locator("[name='categoryListboxContactUs']")
        dropdown_select_category.select_option("Mice")
        dropdown_select_product = page.locator("[name='productListboxContactUs']")
        dropdown_select_product.select_option(index=3)
        contact_us_email = page.locator("[name='emailContactUs']")
        contact_us_email.fill("testemail@gmail.com")
        contact_us_subject = page.locator("[name='subjectTextareaContactUs']")
        contact_us_subject.fill("sigma sigma on the wall who's the skibidiest of them all?")
        contact_us_send_button = page.locator("#send_btn")
        contact_us_send_button.click()
        print("End")
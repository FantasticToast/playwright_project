
class DonationPage:

    def __init__(self, page):
        self.page = page

    def go_to_donation_page(self):
        donation_page_button = self.page.locator("[id='pt-sitesupport-2']")
        donation_page_button.click()

    def change_donation_country(self, country = "United States"):
        change_button = self.page.locator("[id='country-change']")
        change_button.click()
        country_dropdown_list = self.page.locator("[id='country-select']")
        country_dropdown_list.select_option(country)
        change_confirm_button = self.page.locator("[id='country-select-go']")
        change_confirm_button.click()

    def return_lowest_donation_amount_shekels(self):
        list_donation_amount = self.page.query_selector_all("[class='frb-btn']")
        return float(list_donation_amount[3].inner_text().replace("₪", ""))

    def return_second_lowest_donation_amount_shekels(self):
        list_donation_amount = self.page.query_selector_all("[class='frb-btn']")
        return float(list_donation_amount[4].inner_text().replace("₪", ""))
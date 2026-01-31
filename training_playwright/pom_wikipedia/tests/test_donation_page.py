from training_playwright.pom_wikipedia.pages.donation_page import DonationPage


class TestDonationPage:

    def test_change_donation_country(self, setup_playwright):
        page = setup_playwright
        donation_page = DonationPage(page)
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        donation_page.go_to_donation_page()
        donation_page.change_donation_country()
        assert page.url == "https://donate.wikimedia.org/w/index.php?title=Special%3ALandingPage&country=US&uselang=en&wmf_medium=sidebar&wmf_source=donate&wmf_campaign=en.wikipedia.org#"

    def test_lowest_donation_amount_smaller_than_second_lowest_shekels(self, setup_playwright): #only works for shekels
        page = setup_playwright
        donation_page = DonationPage(page)
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        donation_page.go_to_donation_page()
        assert donation_page.return_lowest_donation_amount_shekels() < donation_page.return_second_lowest_donation_amount_shekels()

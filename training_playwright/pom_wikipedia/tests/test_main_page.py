import re

from playwright.sync_api import expect

from training_playwright.pom_wikipedia.pages.main_page import MainPage


class TestMainPage:

    def test_search_term(self, setup_playwright):
        page = setup_playwright
        main_page = MainPage(page)
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        main_page.search_wikipedia_term()
        assert page.url == "https://en.wikipedia.org/wiki/Quality_assurance"

    def test_page_appearance_radio_buttons_continuity(self, setup_playwright): #test if page appearance settings persist after page change
        page = setup_playwright
        main_page = MainPage(page)
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        main_page.change_text_size_to_small()
        main_page.change_width_to_wide()
        main_page.change_color_to_dark()
        main_page.random_article()
        assert page.locator("[id='skin-client-pref-vector-feature-custom-font-size-value-0']").is_checked() #check if Small text size radio button is checked
        assert page.locator("[id='skin-client-pref-vector-feature-limited-width-value-0']").is_checked() #check if wide width radio button is checked
        assert page.locator("[id='skin-client-pref-skin-theme-value-night']").is_checked() #check if dark color radio button is checked

    def test_change_language_to_hebrew(self, setup_playwright):
        page = setup_playwright
        main_page = MainPage(page)
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        main_page.change_language_to_hebrew()
        assert page.url == "https://he.wikipedia.org/wiki/%D7%A2%D7%9E%D7%95%D7%93_%D7%A8%D7%90%D7%A9%D7%99"

    def test_random_article_history(self, setup_playwright):
        page = setup_playwright
        main_page = MainPage(page)
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        main_page.random_article()
        main_page.view_page_history()
        expect(page).to_have_title(re.compile("history"))
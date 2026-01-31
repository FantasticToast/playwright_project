
class MainPage():

    def __init__(self, page):
        self.page = page

    def search_wikipedia_term(self, term = "Quality assurance"):
        search_field = self.page.locator("[id='searchInput']")
        search_button = self.page.get_by_role("button", name="search")
        search_field.fill(term)
        search_button.click()

    def return_to_main_page(self):
        main_menu = self.page.locator("[id='vector-main-menu-dropdown-checkbox']")
        main_menu.click()
        main_page_button = self.page.locator("[id='n-mainpage-description']")
        main_page_button.click()

    def random_article(self):
        main_menu = self.page.locator("[id='vector-main-menu-dropdown-checkbox']")
        main_menu.click()
        random_article_button = self.page.locator("[id='n-randompage']")
        random_article_button.click()

    def change_text_size_to_small(self):
        radio_small_text_button = self.page.locator("[id='skin-client-pref-vector-feature-custom-font-size-value-0']")
        radio_small_text_button.click()

    def change_width_to_wide(self):
        radio_wide_width = self.page.locator("[id='skin-client-pref-vector-feature-limited-width-value-0']")
        radio_wide_width.click()

    def change_color_to_dark(self):
        radio_color_dark = self.page.locator("[id='skin-client-pref-skin-theme-value-night']")
        radio_color_dark.click()

    def change_language_to_hebrew(self):
        language_dropdown = self.page.locator("[id='p-lang-btn-checkbox']")
        language_dropdown.click()
        language_dropdown_input = self.page.get_by_placeholder("Search for a language")
        language_dropdown_input.fill("Hebrew")
        searched_language = self.page.get_by_role("link", name="עברית").nth(1)
        searched_language.click()
    def view_page_history(self):
        history_button = self.page.locator("[id='ca-history']")
        history_button.click()

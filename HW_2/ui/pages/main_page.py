from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def create_segment(self, login, password, text):
        """Создание сегмента с предварительным заходом на сайт"""
        self.click(self.locators.ENTER, timeout=12)
        self.login(login, password)
        self.click(self.locators.SEGMENTS)
        self.wait(10)
        self.click(self.locators.CREATE)
        self.click(self.locators.APPS_AND_GAMES)
        self.click(self.locators.PLAYING_AND_PAYING)
        self.click(self.locators.CHECKBOX)
        self.click(self.locators.ADD)
        name = self.find(self.locators.SEGMENT_NAME)
        name.clear()
        name.send_keys("Test_segment_{}".format(text))
        self.click(self.locators.CREATE)

    def delete_segment(self, text, locator):
        """Удаление только что созданного сегмента"""
        self.click(self.locators.UP_CROSS)
        self.click(self.locators.SEG_DEL)






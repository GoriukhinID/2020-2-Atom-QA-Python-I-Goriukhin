import pytest
from tests.base import BaseCase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Test(BaseCase):
    log = 'wykciubkyxznspvuvw@twzhhq.online'
    passw = 'Qwe123rty%*'

    @pytest.mark.UI
    @pytest.mark.parametrize('login', ['wykciubkyxznspvuvw@twzhhq.online', 'not_exist@aa.bk'])
    def test_login(self, login):
        """Проверка входа в личный кабинет"""
        self.base_page.click(self.base_page.locators.ENTER, timeout=12)
        self.base_page.login(login, self.passw)
        if login == self.log:
            assert self.base_page.find(self.base_page.locators.YOU_LOGGED)
        else:
            assert self.base_page.find(self.base_page.locators.LOGIN_ERROR)

    @pytest.mark.UI
    def test_create_segment(self):
        """Тест на создание сегмента в аудиториях"""
        identificator = "create"
        locator_to_segment = (By.XPATH,
                              '//a[@title="Test_segment_{}"]'.format(identificator))
        self.main_page.create_segment(self.log, self.passw, identificator)
        assert self.main_page.find(locator_to_segment)
        self.main_page.delete_segment(identificator, locator_to_segment)

    @pytest.mark.UI
    def test_delete_segment(self):
        """Тест на удаление сегмента"""
        identificator = "delete"
        locator_to_segment = (By.XPATH, '//a[@title="Test_segment_{}"]'.format(identificator))
        self.main_page.create_segment(self.log, self.passw, identificator)
        self.main_page.delete_segment(identificator, locator_to_segment)
        self.driver.refresh()
        with pytest.raises(TimeoutException):
            self.base_page.find(locator_to_segment)



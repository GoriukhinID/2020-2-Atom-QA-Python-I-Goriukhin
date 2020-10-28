from selenium.webdriver.common.by import By


class BasePageLocators(object):
    ENTER = (By.XPATH, '//div[contains(@class,"responseHead") and contains(text(), "Войти")]')
    LOGIN = (By.XPATH, '//*[@name="email"]')
    PASSWORD = (By.XPATH, '//*[@type="password"]')
    LOG_IN = (By.XPATH, '//div[contains(@class,"authForm") and contains(text(), "Войти")]')
    YOU_LOGGED = (By.XPATH, '//*[contains(text(), "С чего начать?")]')
    LOGIN_ERROR = (By.XPATH, '//*[contains(text(), "Invalid login or password")]')


class MainPageLocators(BasePageLocators):
    TO_CHOOSE = (By.XPATH, '//span[contains(text(), "Ещё")]')
    SEGMENTS = (By.XPATH, '//a[contains(text(), "Аудитории")]')
    CREATE = (By.XPATH, '//div[contains(text(), "Создать сегмент")]')
    APPS_AND_GAMES = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    PLAYING_AND_PAYING = (By.XPATH, '//span[contains(text(), "Игравшие и платившие в платформе")]')
    CHECKBOX = (By.XPATH, '//input[@value="pay" and @type="checkbox"]')
    ADD = (By.XPATH, '//div[contains(text(), "Добавить сегмент")]')
    SEGMENT_NAME = (By.XPATH, '//input[@maxlength="60"]')
    DELETE = (By.XPATH, '//span[contains(text(), "удалить все")]')
    DEL_CONF = (By.XPATH, '//span[@data-loc-ru="удалить"]')
    SEGMENT_LIST = (By.XPATH, '//a[contains(text(), "Список сегментов")]')
    UP_CROSS = (By.XPATH, '//div[contains(@style, "top: 0px")]/span[contains(@class, "icon-cross cells")]')
    """Локатор к самому верхнему крестику"""
    SEG_DEL = (By.XPATH, '//div[contains(text(),"Удалить")]')








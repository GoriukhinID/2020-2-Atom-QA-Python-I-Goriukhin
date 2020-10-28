import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    download_dir = config['download_dir']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")

        prefs = {"download.default_directory": download_dir}
        options.add_experimental_option('prefs', prefs)

        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install(),
                                  options=options,
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    # quit = закрыть страницу, остановить browser driver
    # close = закрыть страницу, бинарь browser driver останется запущенным
    driver.quit()



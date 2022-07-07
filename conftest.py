import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default="en")


options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': "language"})


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

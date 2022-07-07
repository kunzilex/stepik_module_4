import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def get_chrome_options():
    options = chrome_options
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=800,600')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver



    # usr->local->bin

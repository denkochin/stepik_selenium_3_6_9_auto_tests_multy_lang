import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # possible_languages = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]
    language = request.config.getoption("language")
    # language = None
    # if language in possible_languages:
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    print(f"\nstart chrome browser({language}) for test..")
    browser = webdriver.Chrome(options=options)
    # else:
    #     raise pytest.UsageError("There is no such a language option")
    yield browser
    print("\nquit browser..")
    browser.quit()
from selenium import webdriver
from source.library.constants import Constants


def get_driver(browser_name, url):
    driver = None
    if browser_name == "Chrome":
        driver = webdriver.Chrome(executable_path=Constants.CHROME_PATH)
        driver.maximize_window()
    elif browser_name == "FireFox":
        driver = webdriver.Firefox(executable_path=Constants.FIREROX_PATH)
    driver.get(url)
    driver.implicitly_wait(30)

    return driver
from allure import step
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, web_driver):
        self.driver = web_driver
        self.driver.set_page_load_timeout(30)

    __logout_link = (By.ID, "logoutLink")

    @step
    def click_logout_link(self):
        self.driver.find_element(*self.__logout_link).click()

    @step
    def wait_for_element_to_presence(self, element):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(ec.presence_of_element_located((element[0], element[1])), )
        except TimeoutException:
            print("Element is not present in the DOM after 30 sec", TimeoutException)
            assert False

    @step
    def verify_title(self, expected_title):
        try:
            wait = WebDriverWait(self.driver, 30)
            flag = wait.until(ec.title_contains(expected_title), "Verifying the title")
            assert flag == True
        except:
            print("Title is not matching: /n", expected_title)
            assert False

    '''
        
    '''
    @step
    def verify_text(self, actual_text, expected_text):
        try:
            assert expected_text in actual_text
        except:
            print("Expected: ", expected_text, " is not equal to ", actual_text)
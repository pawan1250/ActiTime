import pytest
from datetime import datetime
import os
from source.library.constants import Constants


class MyPlugin:
    def pytest_sessionfinish(self):
        allure_report = Constants.ALLURE_HTML_PATH + \
                        datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        commond = "allure generate "+Constants.ALLURE_JASON_PATH + \
                  "--output "+ allure_report
        os.popen(commond)

arguments = ['-s', '-v', '--alluredir', Constants.ALLURE_JASON_PATH]

pytest.main(args=arguments, plugins=[MyPlugin()])
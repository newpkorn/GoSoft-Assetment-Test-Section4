import os
import chromedriver_binary
import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver

from selenium_helper import SeleniumHelper

@pytest.fixture(scope='function')
def driver():
    current_dir = os.getcwd()
    if "resources" in current_dir:
        while not current_dir.endswith("resources"):
            current_dir = os.path.dirname(current_dir)
    else:
        while not current_dir.endswith("resources"):
            current_dir = os.path.dirname(current_dir)
            list_subfolders_with_paths = [f.path for f in os.scandir(current_dir) if f.is_dir()]
            for folder in list_subfolders_with_paths:
                for sub_folder in [f.path for f in os.scandir(folder) if f.is_dir()]:
                    if sub_folder.endswith("resources"):
                        current_dir = sub_folder
                        break

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options)
    driver.get('file:///' + os.path.join(current_dir, '__files', 'index.html'))
    print('nowy driver')
    return driver
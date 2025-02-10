from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumExtractor:
    
    def __init__(self, driver):
        self.driver = driver

    def click_send_button(self):
        send_button = self.driver.find_element(By.XPATH, "//button[text()='Send']")
        send_button.click()

    def get_information_from_hq(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.ID, "result").text.strip() != ""
        )
        return self.driver.find_element(By.ID, "result").text

    def get_animals(self):
        animals = self.driver.find_elements(By.XPATH, "//h4/following-sibling::div[@class='container main']//div")
        return [animal.text for animal in animals if animal.is_displayed()]

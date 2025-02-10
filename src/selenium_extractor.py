import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumExtractor:
    
    def __init__(self, driver):
        self.driver = driver

    def click_send_button(self):
        # Find the "Send" button and click it to trigger the data fetch
        send_button = self.driver.find_element(By.XPATH, "//button[text()='Send']")
        send_button.click()

    def get_information_from_hq(self):
        print("Clicking send button")  # debug to see if the button is clicked
        self.click_send_button()
        
        # Wait for the result to appear
        time.sleep(2)
        
        result_text = self.driver.find_element(By.ID, "result").text
        print(f"Result text after waiting: {result_text}")  # debug to see if the result is fetched
        
        return result_text


    def get_animals(self):
        # Find all animal names inside the 'Animals to monitor' section under the 'container main' class
        animals = self.driver.find_elements(By.XPATH, "//h4/following-sibling::div[@class='container main']//div[@class='container']")
        animal_names = [animal.text for animal in animals]
        return animal_names

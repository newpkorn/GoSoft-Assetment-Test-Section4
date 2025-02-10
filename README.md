#Python Selenium Advanced topics

## Introduction
You are working for a zoo. For that zoo's clinic, there is a system that informs which animals need to be checked during the current hour, as well as a system connected to the caretakers' station that fetches data from their station on demand. The data is then displayed back to the user who initiated the query. 
Implement two methods in the SeleniumExtractor class (`/src/selenium_extractor.py`), that should use Selenium WebDriver to peform actions on the `/resources/__files/index.html` page. Assume that the page is already loaded by the driver.

## Tasks:
1. Click the button in the `h2` section and then extract the resulting text and return it from the function.
2. Return a list with all WebElements containing animal names in the `h4` section that contains the animals that need to be checked within the current hour. 
import pytest

from selenium_helper import SeleniumHelper
from src.selenium_extractor import SeleniumExtractor


@pytest.mark.usefixtures("driver")
class TestSelenium:

    def test_get_all_visible_animals(self, driver):
        extractor = SeleniumExtractor(driver)
        animals = extractor.get_animals()
        assert len(animals) == 2

    def test_read_from_hq_api(self, driver):
        extractor = SeleniumExtractor(driver)
        extractor.click_send_button()
        text = extractor.get_information_from_hq()
        assert text == SeleniumHelper.data

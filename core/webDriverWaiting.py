from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverWaiting:
    def __init__(self, driverInstance):
        self.driver = driverInstance
        self.timeout = 10000

    def elementIsLocated(self, element):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(element))
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(element))
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(element))

    def elementIsStale(self, selector):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(selector)
        )
        WebDriverWait(self.driver, self.timeout).until(
            EC.staleness_of(element)
        )

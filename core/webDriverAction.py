from core.webDriverWaiting import WebDriverWaiting

class WebDriverAction:
    def __init__(self, driverInstance):
        self.driver = driverInstance
        self.waitings = WebDriverWaiting(driverInstance)

    def navigateTo(self, url):
        self.driver.get(url)

    def clickOnElement(self, element):
        self.waitings.elementIsLocated(element)
        self.driver.find_element(*element).click()

    def sendKeys(self, element, value):
        self.waitings.elementIsLocated(element)
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)

    def closeWindow(self):
        self.driver.quit()
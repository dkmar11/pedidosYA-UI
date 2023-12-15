from core.webDriverAction import WebDriverAction
from core.webDriverWaiting import WebDriverWaiting
from selenium.webdriver.common.by import By

def login(driver, email, passd):

    action = WebDriverAction(driver)
    waiting = WebDriverWaiting(driver)
    
    user = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.CSS_SELECTOR, "input[name='password']")
    loginButton = (By.CSS_SELECTOR, "button[type='submit']")
    splash = (By.ID, "splash")
    loader = (By.CSS_SELECTOR, "div[class*='LoaderWrapper']")

    action.navigateTo("https://bo.usehurrier.com/app/rooster/web/login")
    waiting.elementIsStale(splash)
    action.sendKeys(user, email)
    action.sendKeys(password, passd)
    action.clickOnElement(loginButton)
    waiting.elementIsStale(loader)
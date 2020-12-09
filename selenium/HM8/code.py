from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import Config


class BasePage:

    def __init__(self, browser):
        self.browser = browser


    def find_element(self, locator,time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
    
    def click(self, by_locator, time=10):
        WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(by_locator)).click()
    

class GLCareersResultPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        
  
    @property
    def cookies_button(self):
        return self.find_element(Config.COOKIES_ALLOW_ALL_BUTTON)

    @property
    def search_field(self):
        return self.find_element(Config.SEARCH_FIELD)
    
    @property
    def search_button(self):
        return self.find_element(Config.SEARCH_BUTTON)

 
    def open(self):
        self.browser.get(Config.BASE_URL)
        self.click(Config.COOKIES_ALLOW_ALL_BUTTON)
    
    def search_vacancy(self, vacancy):
        self.search_field.send_keys(vacancy)
        self.click(Config.SEARCH_BUTTON)
    

driver = webdriver.Chrome()
careersPage = GLCareersResultPage(driver)
careersPage.open()
careersPage.search_vacancy('QA')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://www.globallogic.com/ua/careers/'


    def find_element(self, locator,time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
    
    def click(self, by_locator, time=10):
        WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(by_locator)).click()
    
    def getFirst(self):
        return self.browser.get(self.base_url)

class GLCareersResultPage(BasePage):
    SEARCH_FIELD = (By.ID, "by_keyword")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="hero"]/div/div/div/div/div/div/div/form/div/button')
    COOKIES_ALLOW_ALL_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    def __init__(self, browser):
        super().__init__(browser)
        0
  
    @property
    def cookies_button(self):
        return self.find_element(GLCareersResultPage.COOKIES_ALLOW_ALL_BUTTON)

    @property
    def search_field(self):
        return self.find_element(GLCareersResultPage.SEARCH_FIELD)
    
    @property
    def search_button(self):
        return self.find_element(GLCareersResultPage.SEARCH_BUTTON)

 
    def open(self):
        self.getFirst()
        self.click(GLCareersResultPage.COOKIES_ALLOW_ALL_BUTTON)
    
    def search_vacancy(self, vacancy):
        self.search_field.send_keys(vacancy)
        self.click(GLCareersResultPage.SEARCH_BUTTON)
    

driver = webdriver.Chrome()
careersPage = GLCareersResultPage(driver)
careersPage.open()
careersPage.search_vacancy('QA')

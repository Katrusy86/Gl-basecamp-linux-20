
from selenium.webdriver.common.by import By

class Config:
    BASE_URL = "https://www.globallogic.com/ua/careers/"
    SEARCH_FIELD = (By.ID, "by_keyword")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="hero"]/div/div/div/div/div/div/div/form/div/button')
    COOKIES_ALLOW_ALL_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
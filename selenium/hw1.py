from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/katrin/Desktop/driver/chromedriver')
driver.get("https://google.com/")
driver.find_element_by_name("q").send_keys("selenium ubuntu python" + Keys.RETURN)
first_result = driver.find_element_by_css_selector("h3")
first_result.click()
first_result = driver.find_element_by_partial_link_text('pypi')
driver.find_element_by_name("q").send_keys("selenium" + Keys.RETURN)
second_result = driver.find_element_by_xpath("(//a[@class='package-snippet'])[2]")
# second_result = driver.find_element_by_partial_link_text('selenium-firefox') 
second_result.click()
driver.close()

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/User/PycharmProjects/untitled1/driver/chromedriver.exe")
driver.get("https://www.google.ru/")
element=driver.find_element_by_name("q")
element.send_keys('tree')
element.send_keys(Keys.ENTER)
element=driver.find_element_by_css_selector("#hdtb-msb-vis > div:nth-child(2) > a")
element.click()
time.sleep(4)
driver.quit()
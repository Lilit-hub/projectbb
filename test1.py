from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/User/PycharmProjects/untitled1/driver/chromedriver.exe")
driver.get("https://www.google.ru/")
driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys("tree")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.find_element_by_css_selector("#hdtb-msb-vis > div:nth-child(2) > a").click()
time.sleep(4)
driver.quit()
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/User/PycharmProjects/untitled1/driver/chromedriver.exe")
driver.get("https://www.demoblaze.com/?fbclid=IwAR3yZhWvRJDLw3A908n1RWHD53uj9FxBxe6PyGfoPk8KbZ1mD82yFvo9Iac")
driver.find_element_by_id("login2").click()
driver.find_element_by_id("loginusername").send_keys("lilitmariam")
driver.find_element_by_id("loginpassword").send_keys("lilit2019")
driver.find_element_by_css_selector("#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
time.sleep(4)
driver.quit()

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/User/PycharmProjects/untitled1/driver/chromedriver.exe")
driver.get("https://www.livescore.com/")
driver.find_element_by_xpath("//div[@data-type='top-menu']//a[@href='/tennis/']").click()
driver.find_element_by_xpath("//ul[@class='buttons btn-light']//a[@href='/tennis/australian-open/']").click()
lists = driver.find_elements_by_xpath("//div[@class='ply']")
for elem in lists:
    print(elem.text)
    time.sleep(1)
    break
driver.quit()
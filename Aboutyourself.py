from selenium import webdriver
import time
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Edge()
time.sleep(2)
driver.maximize_window()
url=" https://sagar-test-qa.vercel.app/about.html"
driver.get(url)
time.sleep (1)

#Locators

fullname=driver.find_element[By.ID, 'fullname']
phone=driver.find_element[By.ID, 'phone']
email=driver.find_element[By.ID, 'email']
hobby=driver.find_element[By.ID, 'hobby']

time.sleep(4)
driver.quit()










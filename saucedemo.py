from selenium import webdriver
import time
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Edge()
time.sleep(2)
driver.maximize_window()
url= "https://www.saucedemo.com/"
driver.get(url)
time.sleep (1)
#Locators


username=driver.find_element(By. XPATH, "//*[@id='user-name'] ")
password =driver.find_element(By. XPATH, "//*[@id='password'] ")

wait =WebDriverWait(driver, 10)
login_button=wait.until (EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))

#Actions

username.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(4)
action=ActionChains(driver)
action.context_click(login_button).perform()

time.sleep(3)




assert "inventory" in driver.current_url, " Login failed "
    
driver.quit()









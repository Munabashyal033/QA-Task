from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui select 
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

wait = WebDriverWait(driver, 10)
login_button=wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))

login_button.click()

time.sleep(2)

dropdown=driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select")
select=any(dropdown)
select.Select_by_Value()





if "inventory" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")
  
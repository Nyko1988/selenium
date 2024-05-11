from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
input_accept = driver.find_element(By.ID, "L2AGLb")
input_accept.click()

input_google = driver.find_element(By.XPATH, "//textarea[@name='q']")
input_google.send_keys("Iphone")
input_google.send_keys(Keys.ENTER)
#time.sleep(5)
assert "Iphone - Пошук Google" in driver.title
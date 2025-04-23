import time

from selenium import webdriver
from selenium.webdriver.common.by import By

drivers = webdriver.Chrome()
drivers.maximize_window()
drivers.get("https://omayo.blogspot.com/")
drivers.find_element(By.ID,"ta1").send_keys("My name is Pallavi")
drivers.find_element(By.NAME,"q").send_keys("Pallavi")
drivers.find_element(By.XPATH,"//input[@value='Search']").click()
drivers.get("https://omayo.blogspot.com/")
drivers.find_element(By.CLASS_NAME,"dropbtn").click()
time.sleep(5)
drivers.find_element(By.LINK_TEXT,"Facebook").click()
time.sleep(5)
drivers.quit()
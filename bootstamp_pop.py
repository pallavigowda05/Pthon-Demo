import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://practice-automation.com/modals/")
driver.find_element(By.ID,"simpleModal").click()
time.sleep(4)
info_pop = driver.find_element(By.ID,"pum_popup_title_1318")
print(info_pop.text)
sec_info=driver.find_element(By.XPATH,"//div[@id='pum_popup_title_1318']/following::p").text
print(sec_info)
driver.find_element(By.XPATH,"(//button[@type='button']) [4]")
time.sleep(5)
driver.quit()

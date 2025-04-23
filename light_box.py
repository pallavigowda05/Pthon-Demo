import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.apple.com/in/shop/buy-mac?afid=p238%7Cs6oYLDFxV-dc_mtid_187079nc38483_pcrid_731778633753_pgrid_113271655127_pntwk_g_pchan__pexid__ptid_kwd-323492926067_&cid=aos-IN-kwgo-mac--slid---product-")
time.sleep(3)
driver.find_element(By.XPATH,"//img[@loading='lazy']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='rc-overlay-closesvg']").click()
driver.close()
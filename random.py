from selenium import webdriver
import time

driver = webdriver.Chrome("D:/unit_testing/chromedriver.exe")
driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://krishnakoustub.wixsite.com/website/")






time.sleep(10)

driver.close()

driver.quit()

print("Test completed") 



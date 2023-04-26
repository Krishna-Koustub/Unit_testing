from selenium import webdriver
import time

driver = webdriver.Chrome("D:/unit_testing/chromedriver.exe")
driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_id("txtusername").send_key("Admin")

driver.find_element_by_id("txtpassword").send_key("admin123")

driver.find_element_by_id("bthlogin").click()

driver.find_element_by_id("welcome").click()

driver.find_element_by_link_test("logout").click()

time.sleep(10)

driver.close()

driver.quit()

print("Test completed") 
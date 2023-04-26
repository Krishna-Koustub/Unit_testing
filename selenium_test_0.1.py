from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import by
from webdriver_manager.chrome import chromeDriverManager 
import time

def test_google():
    driver=webdriver.chrome(chromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.co.in")
    assert driver.title =="Google"
    driver.quit()


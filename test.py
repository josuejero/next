from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.maximize_window()
driver.get("https://google.com")
driver.get("https://youtube.com")
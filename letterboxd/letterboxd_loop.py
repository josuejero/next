from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from letterboxd_json import *


PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.headless = True
driver = webdriver.Chrome(PATH, options=options)


x=1
while True:
    try:
        url = f"https://letterboxd.com/films/popular/size/large/page/{x}/"
        driver.get(url)
        # WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//*[@class=\"frame\"]")))
        time.sleep(5)
        elems = driver.find_elements_by_xpath("//*[@class=\"frame\"]")
        for elem in elems:
            dictionary(elem.get_attribute("href"))
    except:
        print("ERROR")
        time.sleep(1)
        continue
    x+=1


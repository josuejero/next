from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from letterboxd_json import *
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.headless = True
driver = webdriver.Chrome(PATH, options=options)

url = "https://letterboxd.com/films/popular/size/large/page/1/"

driver.get(url)

# WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//*[@class=\"frame\"]")))

time.sleep(5)

for element in driver.find_elements_by_xpath("//*[@class=\"frame\"]"):
    dictionary(element.get_attribute("href"))

with open("letterboxd/useful_data.json",'r+') as file:
        data = json.load(file)

        data["useful_data"].sort(key=operator.itemgetter('Rating'))

        json.dump(data, file, indent=2)
driver.quit()
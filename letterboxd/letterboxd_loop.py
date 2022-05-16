from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint
from letterboxd_json import letterboxd_json
from selenium.webdriver.common.by import By

l_json = letterboxd_json()

url = "https://letterboxd.com/films/popular/size/large/"

soup = BeautifulSoup(requests.get(url).text, "html.parser")

# options = Options()

# options.add_argument('--no-sandbox')

# options.add_argument('--disable-dev-shm-usage')

# options.headless = True

driver = webdriver.Chrome(
    "C:\Program Files (x86)\chromedriver.exe")

driver.get(url)

elements = driver.find_elements(By.CLASS_NAME, "frame")

element_list = []

for elem in elements:
    try:
        element_list.append(elem.get_attribute("href"))
    except:
        break

driver.quit()

print("\n\n\n")

pprint(element_list)

for x in element_list:
    l_json.dictionary(x)


# there is something wrong with the way i use the driver get method

print("\n\n\n")

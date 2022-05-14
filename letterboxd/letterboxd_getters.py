from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re

options = Options()
options.headless = True
driver = webdriver.Chrome(
    "C:\Program Files (x86)\chromedriver.exe", options=options)


def get_title(soup):
    try:
        for title in soup.findAll('h1', {'class': 'headline-1 js-widont prettify'}):
            return title.string
    except:
        return 'ERROR'


def get_release_year(soup):
    try:
        for year in soup.findAll('small', attrs={'class': 'number'}):
            return int(year.find('a').contents[0])
    except:
        return 'ERROR'


def get_number_of_members(url):
    driver.get(url)
    while True:
        try:
            return int(re.sub('[^0-9,]', "", WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@id=\"js-poster-col\"]/section[1]/ul/li[1]/a"))).get_attribute("data-original-title")).replace(",", ""))
        except:
            driver.refresh()
            continue


def get_rating(url):
    driver.get(url)
    while True:
        try:
            return float(WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@id=\"film-page-wrapper\"]/div[2]/aside/section[2]/span/a"))).get_attribute("textContent"))
        except:
            driver.refresh()
            continue


def does_banner_exist(soup):
    if soup.findAll('div', attrs={'class': 'backdropmask js-backdrop-fade'}):
        return True
    else:
        return None

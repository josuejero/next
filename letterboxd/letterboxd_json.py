from letterboxd_getters import *
import requests
from bs4 import BeautifulSoup
import json

url = "https://letterboxd.com/film/mulan/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")


def dictionary():

    data = {
        'Title': get_title(soup),
        'Year': get_release_year(soup),
        'Rating': get_rating(url),
        'Members': get_number_of_members(url),
        'Banner': does_banner_exist(soup)
    }
    driver.close()
    print("\n", json.dumps(data, indent=2), "\n")

    with open("letterboxd/test.json", "w") as outfile:
        json.dump(data, outfile)

    with open('letterboxd/test.json','r+') as f:
        dic = json.load(f)
        dic.update(data)
        json.dump(dic, f)

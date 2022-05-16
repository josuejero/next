from letterboxd_getters import *
import requests
from bs4 import BeautifulSoup
import json


def dictionary(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    driver.get(url)

    data = {
        'Title': get_title(soup),
        'Year': get_release_year(soup),
        'Rating': get_rating(url),
        'Members': get_number_of_members(url),
        'Banner': does_banner_exist(soup)
    }
    print("\n", json.dumps(data, indent=2), "\n")


# print("WHY IS THIS PRINTING")
# dictionary("https://letterboxd.com/film/parasite-2019/")
# dictionary("https://letterboxd.com/film/joker-2019/")
# dictionary("https://letterboxd.com/film/knives-out-2019/")
# dictionary("https://letterboxd.com/film/pulp-fiction/")
# dictionary("https://letterboxd.com/film/fight-club/")
# dictionary("https://letterboxd.com/film/spider-man-into-the-spider-verse/")
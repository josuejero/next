from letterboxd_getters import *
import requests
from bs4 import BeautifulSoup
import json


def dictionary(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    with open('letterboxd/movie_data.json', 'w') as f:
        json.dump(json.loads(soup.find('script', {"type" : "application/ld+json"}).get_text().replace("/* <![CDATA[ */", "").replace("/* ]]> */","")), f)

    data = {
        'Title': get_title(),
        'Year': get_release_year(),
        'Rating': get_rating(),
        'Members': get_number_of_members(),
        'Banner': does_banner_exist(soup)
    }
    print("\n", json.dumps(data, indent=2), "\n")
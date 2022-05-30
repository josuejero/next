from ast import operator
from letterboxd_getters import *
import requests
from bs4 import BeautifulSoup
import json, operator

def write_json(new_data, filename='letterboxd/useful_data.json'):
    with open(filename,'r+') as file:

        file_data = json.load(file)

        file_data["useful_data"].append(new_data)

        file.seek(0)

        json.dump(file_data, file, indent = 2)


def dictionary(url):

    with open('letterboxd/movie_data.json', 'w') as f:
        json.dump(json.loads(BeautifulSoup(requests.get(url).text, "html.parser").find('script', {"type" : "application/ld+json"}).get_text().replace("/* <![CDATA[ */", "").replace("/* ]]> */","")), f)

    data = {
        'Title': get_title(),
        'Year': get_release_year(),
        'Rating': get_rating(),
        'Members': get_number_of_members(),
        'Banner': does_banner_exist(BeautifulSoup(requests.get(url).text, "html.parser"))
    }
    
    write_json(data)
    


if __name__ == "__main__":
    url = "https://letterboxd.com/film/parasite-2019/"
    dictionary(url)
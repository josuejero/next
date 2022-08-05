from bs4 import BeautifulSoup
import requests
from getters import *
import json

def new_dictionary(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    data = {
        'Anime': get_title(soup),
        'Type': get_type(soup),
        'Score': get_score(soup),
        'Members': get_members(soup),
        'Status': get_status(soup),        
        'Aired': get_aired_date(soup),
        'Source': get_source(soup),
        'Adaptation': get_adaptation(soup),
        'Sequel': get_sequel(soup)
    }

    with open('my_anime_list/anime_data.json', 'w') as f:
        json.dump(data, f, indent = 2)

if __name__ == "__main__":
    url = "https://myanimelist.net/anime/25777/Shingeki_no_Kyojin_Season_2"
    new_dictionary(url)
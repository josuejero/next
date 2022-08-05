from bs4 import BeautifulSoup
import requests
from anime_json import *


def get_link(soup):
    for div in soup.findAll('div', {"class":"di-ib clearfix"}):
      try:
        new_dictionary(div.find('a').get('href'))
      except:
        break
    

if __name__ == "__main__":
  url = "https://myanimelist.net/topanime.php?type=bypopularity"

  soup = BeautifulSoup(requests.get(url).text, "html.parser")

  get_link(soup)

import requests
from bs4 import BeautifulSoup
import json

def get_title():
  with open('letterboxd/movie_data.json', 'r') as data:
    return json.load(data)['name']

def get_release_year():
  with open('letterboxd/movie_data.json', 'r') as data:
        return json.load(data)['releasedEvent'][0]['startDate']

def get_number_of_members():
    with open('letterboxd/movie_data.json', 'r') as data:
      return json.load(data)['aggregateRating']['ratingCount']

def get_rating():
  with open('letterboxd/movie_data.json', 'r') as data:
      return json.load(data)['aggregateRating']['ratingValue']

def does_banner_exist(soup):
  if soup.findAll('div', attrs={'class': 'backdropmask js-backdrop-fade'}):
        return True
  else:
        return None
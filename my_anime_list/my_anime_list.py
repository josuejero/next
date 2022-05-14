from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
import json
from datetime import datetime

def get_title(soup):
    try:
        for title in soup.findAll('h1', {'class': 'title-name'}):
            return title.string
    except:
        print("ERROR IN GETTING TITLE")


def get_score(soup):
    try:
        for score in soup.findAll('div', {'class': 'score-label'}):
            return float(score.string)
    except:
        return None

def get_type(soup):
    try:
        return soup('body')[0].find('span', text='Type:').next_sibling.next_sibling.string
    except:
        print("ERROR IN GETTING TYPE")

def get_members(soup):
    try:
        for members in soup.findAll('span', {'class': 'numbers members'}):
            return int(members.find('strong').string.replace(',', ''))
    except:
        print("ERROR IN GETTING MEMBERS")


def get_status(soup):
    try:
        
        if soup('body')[0].find('span', text='Status:').next_sibling.split()[0] == "Not":
            return None
        else:
            return soup('body')[0].find('span', text='Status:').next_sibling.replace("\n  ", "")
    except:
        print("ERROR IN GETTING STATUS")



def get_aired_date(soup):
    try:
        return soup('body')[0].find('span', text='Aired:').next_sibling.replace("\n  ", "")
    except:
        return None


def get_source(soup):
    try:
        if soup('body')[0].find('span', text="Source:").next_sibling.split()[0] == "Original":
            return 'Original'
        else:
            return soup('body')[0].find(
                'span', text="Source:").next_sibling.replace("\n  ","")
    except:
        print("ERROR GETTING SOURCE")


def get_sequel(soup):
    try:
        sequels = []
        for link in soup('body')[0].find('td', text='Sequel:').next_sibling.findAll('a'):
            sequels.append(link.string)
        if not sequels:
            return None
        else:
            return ", ".join(sequels)
    except:
        return None

def get_adaptation(soup):
    try:
        adapt = []
        for ada in soup('body')[0].find('td', text='Adaptation:').next_sibling.findAll('a'):
            adapt.append(ada.string)
        return ", ".join(adapt)
    except:
        return None


def get_alternative(soup):
    try:
        versions = []
        for link in soup('body')[0].find('td', text='Alternative version:').next_sibling.findAll('a'):
            versions.append(link.string)
        if not versions:
            return None
        else:
            return ", ".join(versions)
    except:
        return None


def get_link(soup):
    for a in soup('body')[0].find('td', text='Sequel:').next_sibling.find_all('a', href=True):
        return "https://myanimelist.net" + a['href']


def get_prequel(soup):
    try:
        prequels = []
        for link in soup('body')[0].find('td', text='Prequel:').next_sibling.findAll('a'):
            prequels.append(link.string)
        if not prequels:
            return None
        else:
            return ", ".join(prequels)
    except:
        return None


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
        'Sequel': get_sequel(soup),
        'Prequel': get_prequel(soup),
        'Alternative versions': get_alternative(soup)
    }

    json_object = json.dumps(data, indent=4)
    anime.append(json_object)

    # data_items = data.items()
    # for item in data_items:
    #     print(item)

    if data['Sequel'] is None:
        sys.exit()
    else:
        write_json(data)
        url = get_link(soup)
        return new_dictionary(url)


def write_json(new_data, filename='anime.json'):
    with open(anime.json, 'r+') as file:
        file_data = json.load(file)
        file_data["emp_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

if __name__ == '__main__':

    url = "https://myanimelist.net/anime/918/Gintama"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    anime = []
    new_dictionary(url)


# put json objects into a list
# find out how to title the list
# find a way to sort the list via date of aired   
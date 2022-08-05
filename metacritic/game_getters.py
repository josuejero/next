from bs4 import BeautifulSoup
import requests
headers = {"User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36'}

url = "https://www.metacritic.com/game/pc/disco-elysium-the-final-cut"
soup = BeautifulSoup(requests.get(url, headers=headers).text,"html.parser")




def get_title(soup):
    for title in soup.findAll('script',{'type','application/ld+json'}):
      print(title.string)

if __name__ == "__main__":
  
  get_title(soup)
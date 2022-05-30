from bs4 import BeautifulSoup
import requests
import json

url = "https://letterboxd.com/film/chip-n-dale-rescue-rangers/"

soup = BeautifulSoup(requests.get(url).text, "html.parser")

script_text = soup.find('script', {"type" : "application/ld+json"}).get_text()

# for x in script_text:
#   print(x.get_text())
final = script_text.replace("/* <![CDATA[ */", "").replace("/* ]]> */","")

# print ("initial 1st dictionary", final)
# print ("type of ini_object", type(final))

final_dictionary = json.loads(final)

# print ("final dictionary", str(final_dictionary))
# print ("type of final_dictionary", type(final_dictionary))

with open('data.json', 'w') as f:
    json.dump(final_dictionary, f)

with open('data.json', 'r') as data:
    final = json.load(data)
    print(final['name'])

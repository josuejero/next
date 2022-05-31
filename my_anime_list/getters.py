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

def get_link(soup):
    for a in soup('body')[0].find('td', text='Sequel:').next_sibling.find_all('a', href=True):
        return "https://myanimelist.net" + a['href']
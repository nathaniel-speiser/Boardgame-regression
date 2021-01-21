from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import numpy as np
from fake_useragent import UserAgent
def get_marketplace_data(game_id, print_listings=False):
    """
    Given game id, return list with number of marketplace listings and median price
    """
    ua = UserAgent()
    user_agent = {'User-agent': ua.random}
    url = f'https://www.boardgamegeek.com/xmlapi2/thing?id={game_id}&marketplace=1'
    response=requests.get(url, headers = user_agent)
    if response.status_code > 300:
        print('FAILED: ', game_id)
        #print(response.text)
        return [-1,-1]
    soup = BeautifulSoup(response.text, 'xml')
    listings = [price.parent()[:2] for price in soup.find_all('price', currency='USD')]

    if print_listings:
        for listing in listings:
            print(listing)

    num_listings = len(listings)

    if num_listings == 0:
        return [0,0]

    prices = [float(listing[1]['value']) for listing in listings]
    median_price = np.median(prices)

    return [num_listings, median_price]
def get_category_fans(link):
    """
    Given link to boardgame category page on bgg, returns the number of fans of that category

    """
    url = 'https://boardgamegeek.com'+link
    response=requests.get(url)
    soup=BeautifulSoup(response.text, 'html5lib')
    script=soup.find_all('script')[1]
    cat_info=script.contents[0]
    search_text = '\"numfans\":(\d*)}'
    nf_string = re.search(search_text,cat_info)
    return int(nf_string.group(1))

def make_category_dict():
    """
    Generates dict of num_top most popular game categories
    4 digit code is key, name is value
    """
    category_list = []
    url = 'https://boardgamegeek.com/browse/boardgamecategory'
    response=requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')
    table = soup.find('table', class_='forum_table')
    entries = table.find_all('a')
    for entry in entries:
        category = entry.text
        link = entry['href']
        id_ = int(link.split('/')[-2])
        num_fans = get_category_fans(link)
        category_list.append([id_,category,num_fans])
    category_df = pd.DataFrame(category_list,columns=['category_id','category_name','category_fans'])
    top_categories = category_df.sort_values('category_fans', ascending=False)
    top_categories_dict = pd.Series(top_categories['category_name'].values,
                                    index=top_categories['category_id']).to_dict()
    return top_categories_dict

def drop_categories(categories_dict, drop_list):
    return {code:category for code,category in categories_dict.items() if category not in drop_list}




def code_to_name(categories_dict, code_list):
    """
    Converts list of category codes to a list of names of those categories
    """
    name_list=[categories_dict[code] for code in code_list if (code in categories_dict.keys())]
    return name_list

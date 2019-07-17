import requests
import json
from bs4 import BeautifulSoup

def extract_links(tag):
    url = 'https://www.instagram.com/explore/tags/' + tag + '/?hl=en'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    #print(soup)
    body = soup.find('body')
    script_tag = body.find('script')
    raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
    data = json.loads(raw_string)
    for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
        image_src = post['node']['thumbnail_resources'][1]['src']
        print(image_src)
import requests 
import json

from requests.api import head
from selectorlib import Extractor
from time import sleep
from helpers.UserAgentHelper import UserAgentHelper
from helpers.ProxiesHelper  import ProxiesHelper

def get_page(url):
    response = requests.get(url)

def scrape(url, e): 
    user_agent_helper = UserAgentHelper()
    proxy_helper = ProxiesHelper()

    user_agent = user_agent_helper.get_random_ua()

    print(proxy_helper.get_proxy())

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': user_agent,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    
    while 1:
        try:
            proxy = proxy_helper.get_proxy()
            print("Using proxy {}".format(proxy))
            r = requests.get(url, proxies=proxy, headers=headers, timeout=1.5)
            break
        except:
            pass
    print(r)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)

def search(url):
    # Create an Extractor by reading from the YAML file
    e = Extractor.from_yaml_file('selectors/search_results.yml')
    data = scrape(url, e) 
    print(data)
    products = []
    if data is not None:
        for product in data['products']:
            product['search_url'] = url
            products.append(product)
        json_str = json.dumps(products)
        return json.loads(json_str)

def main():
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=iPhone+11+pro&_sacat=0"
    search_result = search(url)
    print(search_result)

if __name__ == '__main__':
    main()
import requests 
import json
from time import sleep
from helpers.UserAgentHelper import UserAgentHelper
from helpers.ProxiesHelper  import ProxiesHelper

def get_page(url):
    response = requests.get(url)

def scrape(url):
    user_agent_helper = UserAgentHelper()
    proxy_helper = ProxiesHelper()

    print(proxy_helper.get_proxy())

    user_agent = user_agent_helper.get_random_ua()

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

    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    

def main():
    url = 'https://www.ebay.com/itm/294181823731?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20180816085401%26meid%3D1c3f602774e74fb699b993d586bdb965%26pid%3D100970%26rk%3D1%26rkt%3D3%26sd%3D294181823731%26itm%3D294181823731%26pmt%3D0%26noa%3D1%26pg%3D2380057%26brand%3DApple&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3Adf55f033-bd70-11eb-b489-8af2a02fd408%7Cparentrq%3Aa43801f31790a45e3daffed2fff2a76a%7Ciid%3A1'

    scrape(url)



if __name__ == '__main__':
    main()
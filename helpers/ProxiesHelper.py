import requests
from bs4 import BeautifulSoup
from random import choice

class ProxiesHelper: 


    def __init__(self):
        print("init")
    
    def get_proxy(self):
        url = 'https://sslproxies.org/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        return {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
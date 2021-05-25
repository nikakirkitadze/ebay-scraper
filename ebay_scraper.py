

def get_page(url):
    response = requests.get(url)

def main():
    url = 'https://www.ebay.com/itm/294181823731?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20180816085401%26meid%3D1c3f602774e74fb699b993d586bdb965%26pid%3D100970%26rk%3D1%26rkt%3D3%26sd%3D294181823731%26itm%3D294181823731%26pmt%3D0%26noa%3D1%26pg%3D2380057%26brand%3DApple&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3Adf55f033-bd70-11eb-b489-8af2a02fd408%7Cparentrq%3Aa43801f31790a45e3daffed2fff2a76a%7Ciid%3A1'

    get_page(url)



if __name__ == '__main__':
    main()
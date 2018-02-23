# # # #          https://coinmarketcap.com/all/views/all/
# 1. парсер однопоточний
# 2. час
# 3. парсер многопоточний
# 4. експорт в csv
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from multiprocessing import Pool
##
def get_html(url):      ### get html text of our page
    r = requests.get(url)
    return r.text

def get_all_links(html):## return all links from page
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
    links =[]
    for td in tds:
        a ='https://coinmarketcap.com' + td.find('a').get('href') #string
        links.append(a)
    return links
def get_page_data(html):
    soup =BeautifulSoup(html, 'lxml')
    try :
        name = soup.find('h1', class_='text-large').text.strip()
    except: name = ''

    try :
        price = soup.find('span', id='quote_price').text.strip()
    except :
        price = ''

    data = {"name": name,
            "price": price}
    return data
def write_csv(data):
    with open('coinmarket.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['price']))
        print(data['name'], 'parsed!!!', end="")


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def main():
    start_time = datetime.now()
    url ='https://coinmarketcap.com/all/views/all/'

    all_links = get_all_links(get_html(url))
    # for i,url in enumerate(all_links):
    #     html = get_html(url)
    #     data= get_page_data(html)
    #     write_csv(data)
    #     print(i,end='')

    with Pool(30) as p:
        p.map(make_all, all_links)
    end_time = datetime.now()
    total = end_time-start_time
    print(str(total))
main()


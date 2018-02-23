import sys
from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup
import re
def get_html(url):
    r = requests.get(url)
    return r.content

def first_table_output(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    table_header_row=[]
    table = soup.find('table', id='cvssscorestable')
    x=PrettyTable()
    for row in table.findAll('tr'):        # робимо шапку таблиці тобто те що дано в таску
        table_header_row.append(row.find('th').text)
        table_header_row.append(row.find('td').text )#.replace(str(regex),''))
        x.add_row(table_header_row)
        table_header_row.clear()
    print(x)
def second_table_output(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    table_header_row = []
    table_1_row = []
    y = PrettyTable()
    table = soup.find('table',id='vulnprodstable')
    for row in table.findAll('tr'):
        for th in row.findAll('th'):
            if len(th)== 0:
                th = '--'
                table_header_row.append(th)
            else:
                table_header_row.append(th.text)
        for td in row.findAll('td'):
            table_1_row.append(td.text.replace('\t','').replace('\n','').replace('&',''))
        y.field_names =table_header_row
        if len(table_1_row) ==0:
            continue
        else:y.add_row(table_1_row)
        table_1_row.clear()
    return str(y)

def make_all(x,y):
    file = str(sys.argv[1]) + '.txt'
    with open(file,'w') as f:
        f.write(str(x))
        f.write(str(y))
    print(x)
    print(y)


if __name__ == '__main__':
    sys.argv.append('CVE-2007-0994')
    sys.argv.append('CVE-2018-0747')
    for i in range(1,len(sys.argv)):
        url = 'https://www.cvedetails.com/cve/' + str(sys.argv[i])
        table1=first_table_output(get_html(url))
        table2=second_table_output(get_html(url))
        make_all(table1,table2)
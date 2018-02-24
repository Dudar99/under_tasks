import sys
from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup
import re
def get_html(url):
    r = requests.get(url)
    return r.content
# def unuseful(url_1):##########################DELETE
#     f = requests.get(url_1)
#     soup1 = BeautifulSoup(f.content,'lxml')
#     list_of_CVE=[]
#     lost_list=[]
#     CVE_table = soup1.find('table',class_='searchresults')
#     for row in CVE_table.findAll('tr','srrowns'):
#         for td in row.findAll('td' ):
#             list_of_CVE.append(str(td.find('a')).replace('<a name="y2017"> </a>','').replace('None',''))
#     for i in range(1,len(list_of_CVE),15):
#         lost_list.append(list_of_CVE[i].split('/" title')[0].split('/cve/')[1])
#     for i in range(0,len(lost_list)):
#         sys.argv.append(lost_list[i])
#     return sys.argv
def first_table_output(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    table_header_row=[]
    table = soup.find('table', id='cvssscorestable')
    x=PrettyTable()

    reg_exp = r'\([^\)]+\)'
    for row in table.findAll('tr'):        # робимо шапку таблиці тобто те що дано в таску
        table_header_row.append(row.find('th').text)
        string_without_bracket = re.sub(reg_exp,'',row.find('td').text)
        table_header_row.append(string_without_bracket)
        x.add_row(table_header_row)
        table_header_row.clear()
    return x
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

def make_all(x,y,CVE):
    file = str(CVE) + '.txt'
    with open(file,'w') as f:
        f.write(str(x))
        f.write(str(y))
    print("\n\n\n!!!!!!!!!!!!!!!!-------PARSED CVE(",str(CVE),')-------!!!!!!!!!!!!!!!!!!!!!')
    print(x)
    print(y)


if __name__ == '__main__':
    # url_1 = 'https://www.cvedetails.com/vulnerability-list/vendor_id-14/year-2017/IBM.html' ##############DELETEEEEEEEE##
    # unuseful(url_1)

    for i in range(1,len(sys.argv)):
        CVE = sys.argv[i]
        url = 'https://www.cvedetails.com/cve/' + str(sys.argv[i])
        table1=first_table_output(get_html(url))
        table2=second_table_output(get_html(url))
        make_all(table1,table2,CVE)

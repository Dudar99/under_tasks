import re
from collections import Counter
def read_file(filename):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(filename) as inf:
        log = inf.read()
    ip_list = re.findall(regexp, log)
    return ip_list
def top_ip(ip_list):
    ip_top = str(Counter(ip_list))
    return ip_top.split('{\'')[1]
def popular_sites(filename):
    list_of_site=[]
    with open(filename) as inf:
        for i in inf:
            list_of_site.append(i.split('-0800]')[1].split('HTTP')[0])
        top_site = str(Counter(list_of_site))
        print ('Top site:  http://telegra.ph',top_site[16:].split('\':')[0], sep="")
if __name__ == '__main__':
    print ("The top IP is : ", top_ip(read_file('log.txt')).split('\':')[0], ', with : ' ,top_ip(read_file('log.txt')).split('\':')[1].split(',')[0],'requests' )
    popular_sites('log.txt')
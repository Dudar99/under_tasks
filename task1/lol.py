# -*- coding: utf-8 -*-
from collections import Counter
from prettytable import PrettyTable

def reader(filename):
    with open(filename) as f:
        ips = []
        urls = []
        for line in f:
            if len(line) != 1:
                ips.append(line.split(" ")[0])
                urls.append(line.split(" ")[8])
        ips_freq = dict(Counter(ips))
        urls_freq = dict(Counter(urls))

        sorted_ips_freq = sorted(ips_freq.items(), key=lambda t: t[1], reverse=True)
        sorted_urls_freq = sorted(urls_freq.items(), key=lambda t: t[1], reverse=True)

        ips_result_table = PrettyTable(['IP', 'FREQUENCY'])
        urls_result_table = PrettyTable(['URL', 'FREQUENCY'])

        output(sorted_ips_freq, ips_result_table)
        output(sorted_urls_freq, urls_result_table)


def output(sorted_res, table):
    for k, v in sorted_res:
        table.add_row([str(k), str(v)])
    print (table)


if __name__ == '__main__':
reader('log.txt')
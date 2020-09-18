#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests
import re

with open ('./app/templates/index.html', 'r') as f:
    contents = f.read()
    soup = bs(contents, 'lxml')
    string_soup = str(soup)
    e = re.findall(r'(\<\w*\>)|(\<\/\w*\>)', string_soup)
    #m = re.findall(r'', string_soup)
    for entity in e:
        if entity[0] != '':
            print(entity[0])
        elif entity[1] != '':
            print(entity[1])
        else:
            continue

# coding:utf-8
# Author :     microease
# Date :       2019/4/21

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import requests
from bs4 import BeautifulSoup

response = requests.get("http://py4e-data.dr-chuck.net/comments_189317.xml")
soup = BeautifulSoup(response.text, 'xml')

num = []
for count in soup.find_all('count'):
    num.append(count.text.strip())
sum = 0
for i in num:
    sum+=int(i)
print(sum)

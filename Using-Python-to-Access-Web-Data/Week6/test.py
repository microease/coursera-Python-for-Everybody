# coding:utf-8
# Author :     microease
# Date :       2019/4/22
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import requests
from bs4 import BeautifulSoup
import json

response = requests.get("http://py4e-data.dr-chuck.net/comments_189318.json")
data = json.loads(response.text)
comments1 = []
counts = []
for comments in data:
    # comments1.append(data['comments'])
    for count in data['comments']:
        counts.append(count['count'])
print(comments1)
sum = 0

for i in counts:
    sum += i
print(sum/2)

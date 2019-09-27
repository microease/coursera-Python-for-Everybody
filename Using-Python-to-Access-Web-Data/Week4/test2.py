# coding:utf-8
# Author :     microease
# Date :       2019/4/21

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# url = input('Enter - ')
# res = []
# Retrieve all of the anchor tags
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'


# for i in range(5):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     temp_url = []
#     temp = []
#     for tag in tags:
#         temp.append(tag.text)
#         temp_url.append(tag)
#     url = temp_url[2]
#     res.append(temp[2])
# print(res)

def getAllUrl(start_url, times, where):
    url_list = []
    for i in range(times):
        html = urllib.request.urlopen(start_url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        temp_url = []
        for tag in tags:
            temp_url.append(tag['href'])
        url_list.append(temp_url[where - 1])
        start_url = str(temp_url[where - 1])
    print(url_list)


# getAllUrl('http://py4e-data.dr-chuck.net/known_by_Fikret.html', 4, 3)
getAllUrl('http://py4e-data.dr-chuck.net/known_by_Taegan.html', 7, 18)
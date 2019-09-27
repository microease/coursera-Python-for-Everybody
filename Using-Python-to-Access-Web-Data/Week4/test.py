# coding:utf-8
# Author :     microease
# Date :       2019/4/21
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("http://py4e-data.dr-chuck.net/comments_189315.html").read()

soup = BeautifulSoup(response.decode(), 'lxml')
spans = soup('span')
num = []
for span in spans:
    print(span.text)
    num.append(span.text)
print(num)
sum = 0
for i in num:
    sum+=int(i)
print(sum)

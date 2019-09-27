# coding:utf-8
# Author :     microease
# Date :       2019/4/20
import requests
import re
import urllib

response = requests.get("http://py4e-data.dr-chuck.net/regex_sum_189313.txt ")
text = response.text

all_num = re.findall('[0-9]+', text)
print(len(all_num))
sum = 0
for i in all_num:
    sum += int(i)
print(sum)

x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(type(x))
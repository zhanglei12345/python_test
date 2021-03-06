import requests
import re

# get url
url = input('Enter a URL (include `http://`): ')

# connect to the url
website = requests.get(url)

# read html
html = website.text
print(html)

# use re.findall to grab all the links
# findall返回一个列表
links = re.findall('"((http|ftp)s?://.*?)"', html)
print(links)
# output links
for link in links:
    print(link[0])

# 使用 requests模組
import requests
import bs4

url = 'https://www.ptt.cc/bbs/Beauty/index.html'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

data = requests.get(url,headers=header)
data = data.text

htmlfile = bs4.BeautifulSoup(data,'html.parser')
titles = htmlfile.find_all('div',class_='title')
for title in titles:
    print(title.a.string)


# cookie 操作

import urllib.request as req
import bs4
#
url = 'https://www.ptt.cc/bbs/gossiping/index.html'
#
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Cookie':'over18=1'
}
#
data = req.Request(url, headers=header)

with req.urlopen(data) as response:
    datas = response.read().decode('utf-8')

htmlfile = bs4.BeautifulSoup(datas,'html.parser')
titles = htmlfile.find_all('div',class_='title')
for title in titles:
    print(title.a.string)


#
#
# print(datas)
# import requests
#
# url = 'https://www.ptt.cc/bbs/gossiping/index.html'
# data = requests.get(url,headers=header)
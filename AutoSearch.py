import requests
from bs4 import BeautifulSoup
import re
import json

def getHtml(key):
    url = "http://www.baidu.com/s?wd=" + key
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def getData(html):
    soup = BeautifulSoup(html, 'lxml')
    data = []
    for div in soup.find_all('div', {'data-tools':re.compile('title')}):
        info = div.attrs['data-tools']
        dic = json.loads(info)
        data.append(dic['title'])
    return data

def main():
    html = getHtml('江西理工大学')
    ls = getData(html)
    for i in ls:
        print("{}".format(i))

if __name__ == '__main__':
    main()
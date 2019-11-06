from urllib import request
url = 'http://www.baidu.com'
req = request.Request(url)
page = request.urlopen(req).read()
open('baidu.html', 'wb').write(page)


import requests
r = requests.get('http://www.baidu.com')
print(r.status_code)
print(r.encoding)
r.encoding = 'utf-8'
print(r.text)



import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''
url = 'http://www.baidu.com'
print(getHTMLText(url))


from bs4 import BeautifulSoup
import requests
import lxml
r = requests.get('http://www.baidu.com')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
print(soup.a)


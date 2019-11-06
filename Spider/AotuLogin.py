import io
import re
import requests
from PIL import Image
from bs4 import BeautifulSoup
import lxml

class jxustJw:
    def __init__(self):
        self.username = ''
        self.pwd = ''
        self.headers = {

        }

    def getAccount(self):
        fin = open('')
        username = fin.readline().strip()
        pwd = fin.read().strip()
        return username, pwd

    def getYzcode(self, cookies):
        codeUrl = 'http://jw.jxust.edu.cn/verifycode.servlet'
        code = requests.get(codeUrl, headers = self.headers, cookies = cookies)
        # img = Image.open(io.BytesIO(code.content))
        with open('yz.jpg', 'wb') as f:
            f.write(code.content)
        codeText = input("验证码：")
        return codeText

    def firstRequest(self, yzcode, encoded):
        url = ''
        postData = {
            "userAccount" : self.username,
            "userPassword" : '',
            "RANDOMCODE" : yzcode,
            "encoded": encoded
        }
        html = requests.post(url = url, headers = self.headers, postData = postData)
        return html

    def getEncoded(self, cookies):
        encode = ''
        url = ''
        dataStr = ''


    def login(self):
        url = 'http://jw.jxust.edu.cn/'
        res = requests.get(url)
        cookies = res.cookies
        yzcode = self.getYzcode(cookies)
        encoded = self.getEncoded(cookies)
        html = self.firstRequest(yzcode, encoded)
        soup = BeautifulSoup(html.text, 'lxml')


if __name__ == '__main__':
    main = jxustJw()
    main.login()

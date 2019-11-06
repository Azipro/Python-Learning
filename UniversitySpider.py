import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

Uni = []

Rank = []
Quality = []
Result = []
Top = []

Uni_top = []

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as err:
        print(err)

def getUniList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        Univ = []
        for td in ltd:
            Univ.append(td.string)
        if Univ[2] == '江西':
             Uni.append(Univ)
             uni_top = []
             uni_top.append(Univ[1])
             uni_top.append(Univ[9])
             Uni_top.append(uni_top)
        if Univ[1] == '南昌大学' or Univ[1] == '江西农业大学' or Univ[1] == '江西理工大学':
            Rank.append(Univ[0])
            Quality.append(Univ[4])
            Result.append(Univ[5])
            Top.append(Univ[7])


def printUniList(num):
    print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}{5:{0}^10}{6:{0}^10}{7:{0}^10}{8:{0}^10}".format(chr(12288), "排名", "学校", "省市", "总分", "生源质量", "培养结果", "科研规模", "顶尖成果"))
    for i in range(num):
        u = Uni[i]
        print("{1:^3}{2:{0}^11}{3:{0}^4}{4:{0}^8}{5:{0}^10}{6:{0}^15}{7:{0}^10}{8:{0}^12}".format(chr(12288), u[0], u[1], u[2], u[3], u[4], u[5], u[7], u[9]))


def drawing_1(rank, quality, result, top):

    def autolabel(rects, s):
        for rect in rects:
            height = s[int(rect.get_height() % 3)]
            ax.annotate('{}'.format(height),
                        xy = (rect.get_x() + rect.get_width() / 2, height),
                        xytext = (0, 3),
                        textcoords = "offset points",
                        ha = 'center', va = 'bottom')

    labels = ['南昌大学', '江西农业大学', '江西理工大学']

    x = np.arange(len(labels))
    width = 0.4

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, rank, 0.1, label='rank')
    rects2 = ax.bar(x - width / 4, quality, 0.1, label='quality')
    rects3 = ax.bar(x, result, 0.1, label='result')
    rects4 = ax.bar(x + width / 4, top, 0.1, label='top')

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    ax.set_title('南昌大学，江西农业大学，江西理工大学多指标柱状图')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    autolabel(rects1, rank)
    autolabel(rects2, quality)
    autolabel(rects3, result)
    autolabel(rects4, top)

    fig.tight_layout()
    plt.show()


def drawing_2(data):
    sizes = []
    Labels = []
    Explode = []
    for i in data:
        if int(i[1]) != 0:
            Labels.append(i[0])
            sizes.append(i[1])
            if i[0] == '江西理工大学':
                Explode.append(0.5)
            else:
                Explode.append(0)

    labels = tuple(Labels)
    explode = tuple(Explode)

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%',
            shadow = True, pctdistance = 0.9, startangle = 175)
    ax1.axis('equal')

    plt.show()



def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    getUniList(soup)
    printUniList(12)
    drawing_1(Rank, Quality, Result, Top)
    drawing_2(Uni_top)

if __name__ == '__main__':
    main()

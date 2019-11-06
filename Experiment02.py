s1 = input()
s2 = input()
arr1 = s1.split(",")
arr2 = s2.split(",")
arr_f = []
arr_n = []
sum = 0
for i in arr2:
    x = arr1.count(i)
    for j in range(x):
        arr_f.append(int(i))
        sum += 1

if sum < len(arr1):
    for i in arr1:
        x = arr2.count(i)
        if x == 0:
            arr_n.append(int(i))
    arr_n.sort()
    ans = 0
    for i in arr_f:
        print("{},".format(i),end='')
    for i in arr_n:
        if ans != len(arr_n) - 1:
            print("{},".format(i),end='')
            ans += 1
        else:
            print("{}".format(i),end='')
else:
    ans = 0
    for i in arr_f:
        if ans != len(arr_f) - 1:
            print("{},".format(i),end='')
        else:
            print("{},".format(i),end='')


# def getNumSum(n, ans):
# #     if n == 0:
# #         return ans
# #     return getNumSum(int(n / 10), ans + (n % 10))
# #
# # for i in range(2):
# #     n = eval(input())
# #     print(getNumSum(n, 0))




# import jieba
# from wordcloud import WordCloud,ImageColorGenerator
# import matplotlib.pyplot as plt
#
# excludes = {"什么","一个","我们","那里","如今","你们","说道","知道","起来","姑娘","这里","出来",
#             "他们","众人","自己","一面","只见","怎么","两个","没有","不是","不知","这个","听见",
#             "这样","进来","告诉","东西","咱们","就是","奶奶","太太","回来","老太太","大家","只是",
#             "老爷","只得","丫头","这些","不敢","出去"}
# txt = open("红楼梦.txt", "r", encoding="utf-8").read()
# words = jieba.lcut(txt)
# counts = {}
# for word in words:
#     if len(word) == 1:
#         continue
#     rword = word
#     counts[rword] = counts.get(rword, 0) + 1
# for word in excludes:
#     del(counts[word])
# items = list(counts.items())
# items.sort(key = lambda x:x[1], reverse = True)
# lst = []
# for i in range(10):
#     word, count = items[i]
#     lst.append(word)
#
# image = plt.imread('2b.png')
# wc = WordCloud(font_path = r'Fz.TTF',
#                background_color = 'white',
#                max_font_size = 150,
#                mask = image)
#
# txt = ",".join(lst)
# wc.generate(txt)
# img_color = ImageColorGenerator(image)
# wc.recolor(color_func=img_color)
# plt.figure()
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
# wc.to_file(r'D:\Python\Project\Study\wordCloud.png')

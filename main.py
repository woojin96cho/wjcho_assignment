import libs.newsProvider as provider
import pandas as pd

f  = open('./dictionary', 'r', encoding = 'utf-8-sig')
dict = f.readlines()

for i in range(len(dict)):
    dict[i] = dict[i].replace('\n', '')

interest_news = []
all_news=  []

all_news.append(provider.get_yonhapNews())
all_news.append(provider.get_boanNews())

for i in range(len(all_news)):
    for j in range(len(all_news[i])):
        for k in range(len(dict)):
            if dict[k] in all_news[i][j][0]:
                interest_news.append([all_news[i][j][0], all_news[i][j][1]])

print(interest_news)

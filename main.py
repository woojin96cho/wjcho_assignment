import libs.newsProvider as provider
import pandas as pd
import datetime

now = datetime.datetime.now()

f  = open('./dictionary', 'r', encoding = 'utf-8-sig')
dict = f.readlines()

for i in range(len(dict)):
    dict[i] = dict[i].replace('\n', '')

interest_news = pd.DataFrame(columns=["제목", "URL", "제공업체"])
all_news=  []


all_news.append(provider.get_yonhapNews())
all_news.append(provider.get_boanNews())
all_news.append(provider.get_itworld())

for i in range(len(all_news)):
    for j in range(len(all_news[i])):
        for k in range(len(dict)):
            if dict[k] in all_news[i][j][0]:
                interest_news = interest_news.append({"제목":all_news[i][j][0], "URL":all_news[i][j][1], "제공업체":all_news[i][j][2]}, ignore_index=True)

interest_news.index = interest_news.index + 1
print(interest_news)
attach_name = now.strftime('%y%m%d')+"_뉴스.xls"

interest_news.to_excel('./MailAttachment/'+attach_name, encoding='utf-8')

from bs4 import BeautifulSoup
import requests

def ParseNum(num):
    res = 0
    if num.find('K') != -1:
        res = int(float(num[0:num.find('K')]) * 1000)
    elif num.find('M') != -1:
        res = int(float(num[0:num.find('K')]) * 1000000)
    else:
        res = int(num)
    return res

def FindAveragePopularity(tag):
    SumOfCom = 0
    SumOfLikes = 0
    k = 0
    URL = 'https://www.deviantart.com/search/deviations?order=popular-all-time&q={}&page={}'
    for i in range(25):
        a = requests.get(URL.format(tag, i))
        b = BeautifulSoup(a.text, "html.parser")
        page_pictures = b.findAll('div',{'class':'sVdfP'})
        for q in page_pictures:
            SumOfCom += ParseNum(q.find('div', {'title':'comments'}).text)
            SumOfLikes += ParseNum((q.find('div', {'title':'faves'}).text))
            k += 1
    return int(SumOfCom / k), int(SumOfLikes / k), k

import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
import time

base_url = 'https://www.coupang.com/np/search?component=&q={}&channel=user'
keyword = input("검색할 키워드 : ")

params = {
    'q' : keyword,
}

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'    
}
result_list = []
url = base_url.format(keyword,1)
print(url)
res = requests.get(url, headers=headers)
if res.status_code == 200:
    soup = BeautifulSoup(res.text)
    print(soup)
    if(soup.select_one('a.btn-last')):
        last_page = soup.select_one('a.btn-last').text.strip()
    else:
        last_page = 4
    print(last_page)

error_cnt = 0
cp_url = 'https://www.coupang.com/'
for page in range(1, int(last_page)+1):
    url = base_url.format(keyword, page)
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text)
        item_list = soup.select('ul#productList li')
        for item in item_list:
            try:
                item_name = item.select_one('div.name').text.strip()
                link = item.select_one('a').get('href')
                link = parse.urljoin(cp_url, link)
                price = item.select_one('strong.price-value').text.strip()
                price = ''.join(price.split(','))
                result_list.append([item_name, link, price])
            except:
                error_cnt += 1
curr = datetime.now().strftime('%Y-%m-%d')
filename = '쿠팡조회결과_{}_{}.csv'.format(keyword,curr)
df = pd.DataFrame(result_list, columns=['title','link','price'])
df.to_csv(filename, index=False, encoding='euc-kr')
print('fail to save :', error_cnt)
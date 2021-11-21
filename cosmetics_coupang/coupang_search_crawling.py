import requests
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
                item_name = item.select_one('div.name').text.strip() #상품이름
                link = item.select_one('a').get('href')
                link = parse.urljoin(cp_url, link) #상품 링크
                price = item.select_one('strong.price-value').text.strip()
                price = ''.join(price.split(',')) #가격

                img_link = requests.get(link, headers=headers)
                img_link.raise_for_status()
                soup = BeautifulSoup(img_link.text) 
                img_link = "http:"+ soup.select_one('#repImageContainer > img')['src'] #상품 세부 이미지

                print(item_name, price, link, img_link, "\n\n")
                
            except:
                error_cnt += 1
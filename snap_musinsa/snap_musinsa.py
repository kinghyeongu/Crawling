from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import requests
import re
import time

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'    
}

driver = webdriver.Chrome()
PageNum = 1
while PageNum <= 1: # 페이지 넘버를 사용해 자동적으로 페이지가 이동되게 while문 사용
    driver.get(f'https://magazine.musinsa.com/index.php?m=street&style=001&ordw=hit&stx=%ED%95%91%ED%81%AC&_y=2021&_mon=&p={PageNum}#listStart')
    ImgNum = 0
    while ImgNum < 60:
        driver.find_elements_by_css_selector('.articleImg')[ImgNum].click() # 이미지 접속
        time.sleep(2)

        link = driver.current_url
        res = requests.get(link, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text)

        listItem = soup.select(".styleItem-box")
        print(listItem)
        #itemlink = listItem.select_one('a').get('href')

        tbody = soup.select_one('tbody')

        span = tbody.select('span')
        name = str(span[1].text)
        day = str(span[4].text)
        area = str(span[9].text)

        print('이름 : ', name)
        print('촬영일 : ', day)
        print('지역 : ', area)

        url = driver.find_elements_by_css_selector('.lbox')[0].get_attribute('href') # 이미지 URL 따기
        print('이미지url : ', url)

        #print('상세 제품 링크 :', 'https:',listItem)
        print("\n\n")

        

        driver.back() # 뒤로가기
        ImgNum += 1
    PageNum += 1
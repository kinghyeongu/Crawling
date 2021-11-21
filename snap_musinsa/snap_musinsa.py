from bs4 import BeautifulSoup
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
    #ex_snap_pink
    driver.get(f'https://magazine.musinsa.com/index.php?m=street&style=001&ordw=hit&stx=%ED%95%91%ED%81%AC&_y=2021&_mon=&p={PageNum}#listStart')
    ImgNum = 0
    while ImgNum < 60:
        driver.find_elements_by_css_selector('.articleImg')[ImgNum].click() # 이미지 접속
        #time.sleep(2)

        link = driver.current_url
        res = requests.get(link, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text)

        listItem = soup.select_one(".styleItem-box")
        #print(listItem)
        a = listItem.select('a')
        itemname = listItem.select('p')
        
        '''
        deitemimg1 = re.search('href="(.+?)"',str(a[0]))
        if deitemimg1:
            deitemimg1 = deitemimg1.group(1)

        deitemimg2 = re.search('href="(.+?)"',str(a[5]))
        if deitemimg2:
            deitemimg2 = deitemimg2.group(1)

        deitemimg3 = re.search('href="(.+?)"',str(a[10]))
        if deitemimg3:
            deitemimg3 = deitemimg3.group(1)

        deitemimg4 = re.search('href="(.+?)"',str(a[10]))
        if deitemimg4:
            deitemimg4 = deitemimg4.group(1)
        '''
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

        #for문 사용시 json 변환 어려울 것 같음.
        cnt = 0
        for k in range(len(a)):
            if(re.search('title(.+?)"', str(a[k]))):
                cnt = cnt + 1
        
        fir = -5
        for i in range(cnt):
            deitem = re.search('href="(.+?)"',str(a[fir+5]))
            if deitem:
                deitem = deitem.group(1)
                print(itemname[i].text.strip() + " : https:" + deitem)
            fir+=5

        '''
        print('상세 제품1(' + itemname[0].text.strip() + ") : https:" + deitemimg1)
        print('상세 제품2(' + itemname[1].text.strip() + ") : https:" + deitemimg2)
        print('상세 제품3(' + itemname[2].text.strip() + ") : https:" + deitemimg3)
        print('상세 제품3(' + itemname[3].text.strip() + ") : https:" + deitemimg4)
        print(str(a))
        print(cnt)
        '''
        print("\n\n")

        

        driver.back() # 뒤로가기
        ImgNum += 1
    PageNum += 1
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver

driver = webdriver.Chrome()
PageNum = 1
while PageNum <= 1: # 페이지 넘버를 사용해 자동적으로 페이지가 이동되게 while문 사용
    driver.get(f'https://magazine.musinsa.com/index.php?m=street&style=001&ordw=hit&stx=%ED%95%91%ED%81%AC&_y=2021&_mon=&p={PageNum}#listStart')
    ImgNum = 0
    while ImgNum < 60:
        driver.find_elements_by_css_selector('.articleImg')[ImgNum].click() # 이미지 접속
        url = driver.find_elements_by_css_selector('.lbox')[0].get_attribute('href') # 이미지 URL 따기
        urllib.request.urlretrieve(url, "./imgs/" + str(ImgNum)+".jpg")
        driver.back() # 뒤로가기
        ImgNum += 1
    PageNum += 1
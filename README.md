# PersonalColor 프로젝트를 위한 정보 Crawling.
<h3>Coupang, Musinsa 사이트에 필요한 정보를 Crawling 하는 python 프로그램입니다</h3>
- coupang : bs4, requests, selenium<br>
- musinsa : bs4, requests, parse

<br>

## Crawling result
<h3>1. coupang</h3>

![](/imgs/coup1.png)
- 쿠팡 검색창에 필요한 키워드를 입력한다.<br>

![](/imgs/coup3.png)
- 검색한 상품들의 상품명, 가격, 해당링크, 상품이미지까지 크롤링 해온다.

<br><br>
<h3>2. musinsa</h3>

![](/imgs/mu1.png)
- 무신사 브랜드 스냅 코디 키워드를 입력한 사이트의 정보를 셀레니움을 이용해 가져온다.<br>

![](/imgs/mu2.png)
![](/imgs/mu3.png)
![](/imgs/mu4.png)
![](/imgs/mu5.png)
- 또한 코디 마다 인물의 이름, 지역, 이미지, 상세 코디 이름, 이미지를 가져오며, 다음 코디로 넘어간다.

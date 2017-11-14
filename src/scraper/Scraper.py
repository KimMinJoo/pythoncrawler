from bs4 import BeautifulSoup

#분석할 HTML
html='''
<HTML>
<BODY>
<H1 id="title">스크레이핑이란</H1>
<P id="body">웹 페이지를 분석하는 것</P>
<P>원하는 부분을 출력하는 것</P>
</BODY>
</HTML>
'''

#HTML분석
soup = BeautifulSoup(html, 'html.parser')

##태그로 찾기
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 : " + h1.string)
print("p1 : " + p1.string)
print("p2 : " + p2.string)

##ID로 찾기
title = soup.find(id = "title")
body = soup.find(id = "body")

print("title : " + title.string)
print("body : " + body.string)

#여러개 요소 추출하기
html='''
<HTML>
<BODY>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</ul>
</BODY>
</HTML>
'''

soup = BeautifulSoup(html, 'html.parser')

##find_all메소드로 여러요소 추출하기
links = soup.find_all("a")

#링크목록 출력
for link in links:
	href = link.attrs['href']
	text = link.string
	print(text + " > " + href)
#urlretrieve함수를 이용해 바로 저장하기
'''
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url, savename)
print("success")
'''

#rulopen함수를 이용해 파일에 저장하기
'''
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

mem = urllib.request.urlopen(url).read()
with open(savename, mode = 'wb') as f :
	f.write(mem)
	print("success")
'''

#API에서 데이터 얻어오기
'''
import urllib.request
##데이터 읽기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
##바이너리르 문자열로 변환하기
print("============바이너리=============")
print(data)
text = data.decode("utf-8")
print("============문자열=============")
print(text)
'''

#기상청 API이용해서 데이터 얻어오기.
'''
import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
#매개변수를 url 인코딩
values = {
	'stnId' : '108'
}

params = urllib.parse.urlencode(values)

#요청 전용 URL생성
url = API + "?" + params
print(url)

#다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
'''
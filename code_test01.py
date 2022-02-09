import urllib.request

client_id = 'UjWoHN5jEck9VwdK7izN'
client_secret = '7GHOY0ZMQ8'

url = "https://openapi.naver.com/v1/search/news.json?query='BTS'"

req = urllib.request.Request(url) # 네이버서버에 보낼 요청객체를 생성
req.add_header("X-Naver-Client-Id", client_id) # 위에서 만들어진 요청객체에 client_id를 포함시킴
req.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(req) # 네이버서버에 요청객체 req를 전달하여 응답을 받아 reponse에 저장
print(response) # 200이 오면 정상호출 및 승인

ret = response.read().decode('utf-8')
print(ret)
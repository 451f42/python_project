import requests
import random

my_nums = random.sample(range(1, 46), 6) # 리스트 형태로 리턴

url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='
res = requests.get(url).json() # response, 정보를 받아 오는 거니까 get, json이라고 알려줘야 함

drw_nums = []
bns_num = res['bnusNo']

for key, value in res.items():
  if 'drwtNo' in key:
    drw_nums.append(value)
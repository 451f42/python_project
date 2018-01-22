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
    
print(drw_nums, bns_num)

match_cnt = len(set(drw_nums) & set(my_nums))

if match_cnt == 6:
  print('1등')
elif match_cnt == 5 and bns_num in my_nums:
  print('2등')
elif match_cnt == 5 and bns_num not in my_nums:
  print('3등')
elif match_cnt == 4:
  print('4등')
elif match_cnt == 3:
  print('5등')
else:
  print('꽝')
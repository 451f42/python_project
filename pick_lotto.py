import random

# 1-45 범위의 숫자가 담긴 리스트
numbers = list(range(1, 46))

# 6개 뽑기
lucky_numbers = random.sample(numbers, 6)

# 뽑은 6개의 숫자를 정렬
lucky_numbers = sorted(lucky_numbers)

print(lucky_numbers)
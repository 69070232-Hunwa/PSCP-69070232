"""oiurhgourgf"""
import math
member = input()
n = int(input())
total = 0
for i in range(n):
    i += 0
    price = float(input())
    total += price

if member == ("Y"):
    dis = total * 95 / 100
else:
    if total >= 500:
        dis = total * 97 / 100
    else:
        dis = total

final_result = math.ceil(dis * 100) / 100

print(f"{final_result:.2f}")

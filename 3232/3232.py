"""hurehgu8rhguhgu"""
x, y = map(int, input().split())
jump = x
total = 0
count = 0
while total < y and jump > 0:
    total += jump
    count += 1
    jump -= 2
if total >= y:
    print(count)
else:
    print("-1")

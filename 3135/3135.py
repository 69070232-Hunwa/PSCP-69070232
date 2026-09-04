"""rihihkhhiehiehgkfhkfh"""
n, k, t = map(int, input().split())
p = 1
count = 0
while True:
    count += 1
    if p == t:
        break
    p = p + k
    while p > n:
        p = p - n
    if p == 1:
        break
print(count)

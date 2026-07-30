"""snkngggegknk"""

A = int(input())
B = int(input())
d = int(input())
r = int(input())

total = 0

for x in range(A,B + 1):
    if x % d == r:
        total += 1

print(total)

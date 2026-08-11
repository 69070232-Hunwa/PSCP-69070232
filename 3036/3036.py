"""uthpgsh"""

num = int(input())
n = pow(num, 0.5)

if n % 1 > 0:
    n += 1
n = n // 1
n -= 1

wall = n * 2
if ((n + 1) ** 2) % 2 != num % 2:
    wall -= 1
print(int(wall))

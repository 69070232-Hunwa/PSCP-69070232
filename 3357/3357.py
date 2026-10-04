"""Giraffe"""
h = []
n = int(input())
for _ in range(n):
    tall = int(input())
    h.append(tall)
count = 0
for i in range(n):
    if not i:
        if n == 1 or h[i] > h[i + 1]:
            count += 1
    elif i == n - 1:
        if h[i] > h[i - 1]:
            count += 1
    else:
        if h[i] > h[i - 1] and h[i] > h[i + 1]:
            count += 1
print(count)

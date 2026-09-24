"""แปลงดอกไม้"""
L, N = map(int, input().split())
band = 0
total = 0
while total < N:
    band += 1
    first = (band - 1) * L + 1
    last = band * L
    count = L * (first + last) // 2
    total += count
print(band)

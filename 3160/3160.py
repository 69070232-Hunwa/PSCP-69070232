"""ijgiigigii"""
a, b = map(int, input().split())
p = []
for x in range(a, b + 1):
    if x < 2:
        continue
    prime = True
    for i in range(2, x):
        if not x % i :
            prime = False
            break
    if prime:
        p.append(x)
if p:
    print(*p)
print("Total primes:", len(p))

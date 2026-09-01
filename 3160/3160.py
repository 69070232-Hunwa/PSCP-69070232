"""ijgiigigii"""
a, b = map(int, input().split())
p = []
for x in range(a, b + 1):
    if x < 2:
        continue
    prime = True
    for i in range(2, int(x ** 0.5) + 1):
        if not x % i :
            prime = False
            break
    if prime:
        p.append(x)
if p:
    print(*p)
print("Total primes:", len(p))

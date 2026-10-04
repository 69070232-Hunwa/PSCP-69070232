"""Duplicate I"""
m = int(input())
n = int(input())
mm = []
mn = []
result = []
for _ in range(m):
    idm = input()
    mm.append(idm)
for _ in range(n):
    idn = input()
    mn.append(idn)
for x in mm:
    if x in mn:
        result.append(x)
result.sort(reverse=True)
if not result:
    print("Nope")
else:
    for x in result:
        print(x)

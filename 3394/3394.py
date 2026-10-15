"""ส่งต่อ"""
n, s = map(int, input().split())
send = []
for _ in range(n):
    x = int(input())
    send.append(x)
people = []
cur = s
while cur:
    people.append(cur)
    cur = send[cur - 1]
    if cur in people:
        break
print(len(people))

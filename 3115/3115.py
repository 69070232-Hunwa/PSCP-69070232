"""ghuugugufuugu"""

num, _ = map(int, input().split())
store = []
for i in range(num):
    i += 0
    op, close = map(int, input().split())
    store.append((op, close))
time_check = list(map(int, input().split()))
ans = []
for t in time_check:
    count = 0
    for op, close in store:
        if op <= t < close:
            count += 1
    ans.append(count)
print(*ans)

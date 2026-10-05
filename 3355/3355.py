"""Shorten"""
n = []
while True:
    x = int(input())
    if x == -1:
        break
    n.append(x)
if not n:
    print(" ")
else:
    result = []
    first = n[0]
    nexts = n[0]
    for y in n[1:]:
        if y == nexts + 1:
            nexts = y
        else:
            if first == nexts:
                result.append(str(first))
            else:
                result.append(str(first) + "-" + str(nexts))
            first = y
            nexts = y
    if first == nexts:
        result.append(str(first))
    else:
        result.append(str(first) + "-" + str(nexts))
    print(", ".join(result))

"""Point Sorting"""
check = int(input())
for _ in range(check):
    n = int(input())
    point = []
    for _ in range(n):
        x, y = map(int, input().split())
        point.append([x, y])
    for i in range(n):
        for j in range(i + 1, n):
            sum1 = point[i][0] + point[i][1]
            sum2 = point[j][0] + point[j][1]
            if sum1 > sum2:
                point[i], point[j] = point[j], point[i]
            elif sum1 == sum2:
                if point[i][1] < point[j][1]:
                    point[i], point[j] = point[j], point[i]
    for p in point:
        print(p[0], p[1])

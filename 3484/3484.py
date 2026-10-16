"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
n, p = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
total = 0
count = 0
for i in range(n):
    row_sum = 0
    row_count = 0
    for j in range(n):
        row_sum += grid[i][j]
        if grid[i][j] > 0:
            row_count += 1
            count += 1
    total += row_sum
    print(*grid[i], row_count, row_sum)
col_count_list = []
for j in range(n):
    col_count = 0
    for i in range(n):
        if grid[i][j] > 0:
            col_count += 1
    col_count_list.append(col_count)
print(*col_count_list)
col_sum_list = []
for j in range(n):
    col_sum = 0
    for i in range(n):
        col_sum += grid[i][j]
    col_sum_list.append(col_sum)
print(*col_sum_list)
print(count, total, f"{total * p:.2f}")

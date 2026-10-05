"""หั่นขนมปัง"""
w, h, _, _ = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
widths = []
heights = []
left = 0
for i in x:
    widths.append(i-left)
    left = i
widths.append(w-left)
up = 0
for i in y:
    heights.append(i-up)
    up = i
heights.append(h-up)
area = []
for width in widths:
    for height in heights:
        area.append(width * height)
area.sort(reverse=True)
print(area[0], area[1])

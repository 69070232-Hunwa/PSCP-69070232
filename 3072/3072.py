"""guagfulwgu"""

text = input()

total = [0, 0, 0, 0, 0]
sounds = ['a', 'e', 'i', 'o', 'u']

for char in text.lower():
    if char == 'a':
        total[0] += 1
    elif char == 'e':
        total[1] += 1
    elif char == 'i':
        total[2] += 1
    elif char == 'o':
        total[3] += 1
    elif char == 'u':
        total[4] += 1

for i in range(5):
    if total[i] > 0:
        print(f"{sounds[i]} : {total[i]}")

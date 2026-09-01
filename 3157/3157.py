"""gjkjgkgutrjtgtu"""

n = int(input())
SCORE = 0

for i in range(n):
    i += 0
    marks = input()
    if marks == "-":
        SCORE -= 5
    elif marks == "+":
        SCORE += 10

print(SCORE)

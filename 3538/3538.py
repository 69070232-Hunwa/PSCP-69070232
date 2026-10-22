"""B - Fully pair?"""
text = input()
left = ""
for char in text:
    if text.count(char)%2 == 1 and char not in left:
        left += char
if not left:
    print("fully paired")
else:
    print(left)

"""BigFrame"""
t = []
for _ in range(5):
    text = input()
    t.append(text)
n = max(len(text) for text in t)
print("*"*(n+4))
for text in t:
    print("* " + text.ljust(n) + " *")
print("*" * (n + 4))

"""CuteCat CuteFox"""
n = int(input())
first = {
    "Garfield": "Cat01",
    "Fubuki": "Fox01"
}
for _ in range(n):
    animal = input().replace("{", "").replace("}", "")
    animal = animal.replace('"', "").split(":")
    name = animal[0].strip()
    code = animal[1].strip()
    for old_name, old_code in list(first.items()):
        if old_code == code:
            first.pop(old_name)
    first.update({name: code})
cat = {}
fox = {}
for name, code in first.items():
    if code.startswith("Cat"):
        cat.update({name: code})
    else:
        fox.update({name: code})
print("Cat :", len(cat))
print("Fox :", len(fox))
for name, code in sorted(
    cat.items(), key=lambda item: int(item[1][3:])
):
    print(name, ":", code)
for name, code in sorted(
    fox.items(), key=lambda item: int(item[1][3:])
):
    print(name, ":", code)

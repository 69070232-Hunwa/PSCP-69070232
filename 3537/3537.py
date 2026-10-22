"""imposter"""
member = {}
dead = {}
count = 0
while True:
    data = input()
    if data == "Start":
        break
    data = data.replace("{","").replace("}","")
    data = data.replace('"',"").replace(":","")
    name, role = data.split()
    member[name] = role
while True:
    name = input()
    if name == "End":
        break
    if name in member:
        dead[name] = member.pop(name)
for role in member.values():
    if role == "Impostor":
        count += 1
print(count, "Impostor Remains")
print("***Alive***")
for name, role in sorted(member.items()):
    print(name, ":", role)
print("***Dead***")
for name, role in sorted(dead.items()):
    print(name, ":", role)

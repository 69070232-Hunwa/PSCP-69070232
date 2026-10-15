"""Pad Thai"""
myrecipe = []
myflavor = []
while True:
    recipe = input()
    if recipe == "Cook":
        break
    myrecipe.append(recipe)
while True:
    flavor = input()
    if flavor == "End":
        break
    myflavor.append(flavor)
correctrecipe = ["Pad Thai Sauce", "Tofu", "Pickle Turnip",
                  "Shrimp", "Bean Sprouts", "Noodle", "Chives", 
                  "Lime", "Egg", "Oil", "Peanuts"]
correctflavor = ["Sweet", "Sour", "Salty"]
if any(item not in correctrecipe for item in myrecipe):
    print("This is not Pad Thai!!!")
elif any(item not in myrecipe for item in correctrecipe):
    print("This is bad!")
elif (any(taste not in correctflavor for taste in myflavor)
    or any(taste not in myflavor for taste in correctflavor)):
    print("Not Bad...")
else:
    print("Delicious!")

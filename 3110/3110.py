"""jgjkjkjkjsj"""

contry = input()
kg = float(input())

if contry == "BKK CNX":
    TOTAL = (30 * kg) + 10
    print(f"{TOTAL:.2f}")
elif contry == "CNX UBP":
    TOTAL = (40 * kg) + 15
    print(f"{TOTAL:.2f}")
elif contry == "UBP BKK":
    TOTAL = (40 * kg) + 20
    print(f"{TOTAL:.2f}")
elif contry == "BKK PKT":
    TOTAL = (50 * kg) + 25
    print(f"{TOTAL:.2f}")
elif contry == "PKT CNX":
    TOTAL = (60 * kg) + 30
    print(f"{TOTAL:.2f}")
elif contry == "UBP PKT":
    TOTAL = (70 * kg) + 40
    print(f"{TOTAL:.2f}")
else:
    print("Error")

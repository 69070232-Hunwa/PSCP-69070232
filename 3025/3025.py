"""season"""

def season():
    month = int(input())
    date = int(input())

    if month in [1, 2, 3]:
        s = "winter"
    elif month in [4, 5, 6]:
        s = "spring"
    elif month in [7, 8, 9]:
        s = "summer"
    elif month in [10, 11, 12]:
        s = "fall"

    if month % 3 == 0 and date >= 21:
        if s == "winter":
            s = "spring"
        elif s == "spring":
            s = "summer"
        elif s == "summer":
            s = "fall"
        elif s == "fall":
            s = "winter"

    print(s)

season()

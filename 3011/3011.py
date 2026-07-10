"""uututuuh"""

def mix():
    "iguigugu"
    c1 = input().strip()
    c2 = input().strip()
    con = {"Red", "Yellow", "Blue"}

    if c1 not in con or c2 not in con:
        print("Error")
        return

    fcon = {c1, c2}

    if len(fcon) == 1:
        print(c1)
    elif fcon == {"Red", "Yellow"}:
        print("Orange")
    elif fcon == {"Red", "Blue"}:
        print("Violet")
    elif fcon == {"Yellow", "Blue"}:
        print("Green")

mix()

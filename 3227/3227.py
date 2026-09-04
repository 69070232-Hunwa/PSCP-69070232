"""hrgre;ogorjgrgj"""
card = input().upper()
n = len(card)
A1 = ""
A2 = ""
if n == 2:
    if card[0].isalpha():
        if card[0] == "A":
            A1 = "ace"
        elif card[0] == "J":
            A1 = "jack"
        elif card[0] == "Q":
            A1 = "queen"
        elif card[0] == "K":
            A1 = "king"
    else:
        A1 = card[0]
    A2 = card[1]
if n == 3:
    A1 = card[0:2]
    A2 = card[2]

if A2 == "D":
    A2 = "diamonds"
elif A2 == "H":
    A2 = "hearts"
elif A2 == "S":
    A2 = "spades"
elif A2 == "C":
    A2 = "clubs"

print(A1, "of", A2)

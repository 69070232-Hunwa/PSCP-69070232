"""yhy"""

def main():
    """ggjbbj"""
    ti = float(input())
    ui = input()
    uo = input()

    if ui == 'C':
        cel = ti
    elif ui == 'K':
        cel = ti - 273.15
    elif ui == 'F':
        cel = (ti - 32) * 5 / 9
    elif ui == 'R':
        cel = (ti * 5 / 9) - 273.15
    else:
        cel = 0.0

    if uo =='C':
        re = cel
    elif uo == 'K':
        re = cel + 273.15
    elif uo == 'F':
        re = cel * 9 / 5 + 32
    elif uo == 'R':
        re = (cel + 273.15) * 9 / 5
    else:
        re = 0.0

    print(f"{re:.2f}")

main()

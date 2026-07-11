"""giugeg"""

def main():
    """uyeuiuhg"""
    total_score = float(input())
    top = float(input())

    last = total_score - (2 * top)

    if last < 0:
        last = 0

    if top - last > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()

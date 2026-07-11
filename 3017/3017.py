"""dgddgdgid"""

def bill():
    """fgfwfjr"""
    price = int(input().strip())
    service = price * 0.1

    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000

    t1 = price + service
    vat = t1 * 0.07
    total_bill = t1 + vat

    print(f"{total_bill:.2f}")

bill()

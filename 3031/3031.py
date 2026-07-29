"""oiuhtgouhg"""
import math

def main():
    """gfhjdb"""
    S, N = map(int, input().split())
    results = []
    for _ in range(N):
        x, y = map(int, input().split())

        distance = (x ** 2) + (y ** 2)
        area = 3.1416 * distance
        time = area / S
        results.append(math.ceil(time))
    for ans in results:
        print(ans)
main()

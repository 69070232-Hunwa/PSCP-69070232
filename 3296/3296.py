"""RGB Mixed"""
r1, g1, b1 = map(int,input().split())
r2, g2, b2 = map(int,input().split())
rmix = int((r1 + r2)/2)
gmix = int((g1 + g2)/2)
bmix = int((b1 + b2)/2)
print(rmix, gmix, bmix)

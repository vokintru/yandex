x1, y1, r1 = input().split()
x1, y1, r1 = int(x1), int(y1), int(r1)
x2, y2, r2 = input().split()
x2, y2, r2 = int(x2), int(y2), int(r2)

if (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r1 + r2) ** 2:
    print("NO")
else:
    print("YES")

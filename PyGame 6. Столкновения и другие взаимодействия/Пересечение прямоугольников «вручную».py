a = input().split()
b = input().split()

ax1, ay1, ax2, ay2 = a[0], a[1], a[2], a[3]
bx1, by1, bx2, by2 = b[0], b[1], b[2], b[3]

s1 = (bx1 <= ax1 <= bx2) or (bx1 <= ax2 <= bx2)
s2 = (by1 <= ay1 <= by2) or (by1 <= ay2 <= by2)
s3 = (ax1 <= bx1 <= ax2) or (ax1 <= bx2 <= ax2)
s4 = (ay1 <= by1 <= ay2) or (ay1 <= by2 <= ay2)

if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
    print("YES")
else:
    print("NO")

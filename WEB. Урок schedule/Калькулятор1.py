import sys

a = 1
glob = 0
if len(sys.argv) > 1:
    count = 0
    for i in sys.argv:
        count += 1
        try:
            x = int(i)
            if int(sys.argv[count]) // 2 == 1:
                print("+")
                glob += x
            else:
                print("-")
                glob -= x
        except Exception as s:
            if a > 2:
                print(s)
    print(glob)
else:
    print("NO PARAMS")

print("Vvedite znacheniya X and Y: ")
x = float(input("X: "))
y = float(input("Y: "))
if x > 0 and y > 0:
    print("1 chetvert")
elif x > 0 and y < 0:
    print("4 chetvert")
elif x < 0 and y > 0:
    print("2 chetvert")
elif x < 0 and y < 0:
    print("3 chetvert")
else:
    print("na osi")

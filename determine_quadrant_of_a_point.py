x = float(input("Insert coordinate of x point: "))
y = float(input("Insert coordinate of y point: "))


if x > 0 and y > 0:
    print("The first quadrant")
elif x < 0 and y > 0:
    print("The second quadrant")
elif x < 0 and y < 0:
    print("The third quadrant")
elif x < 0 and y < 0:
    print("The fouth quadrant")
elif x == 0:
    print("X point")
elif y == 0:
    print("Y point")
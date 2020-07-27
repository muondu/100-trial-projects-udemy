x = int(input("PLS insert first number:  "))
y = int(input("PLS insert second number:  "))
z = int(input("PLS insert third number:  "))

print("The maximum number is : ", end = "")
if y <= x >= z:
    print(x)
elif x <= y >= z:
    print(y)
elif x <= z >= y:
    print(z)
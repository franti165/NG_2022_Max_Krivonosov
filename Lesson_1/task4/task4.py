a = int(input("Type a= "))
b = int(input("Type b= "))
c = int(input("Type c= "))
if (b * b - 4 * a * c) >= 0:
    x = (-1 * b + (b * b - 4 * a * c)) / (2 * a)
    print("The first root is ", x)
    x = (-1 * b - (b * b - 4 * a * c)) / (2 * a)
    print("The second root is ", x)
else:
    print("The discriminant is less than 0, the roots are immaterial.")
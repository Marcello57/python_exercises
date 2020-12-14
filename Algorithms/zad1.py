from math import sqrt

print("Equation form ax^2 + bx + c")
print("Enter a:")
a = int(input())
print("Enter b:")
b = int(input())
print("Enter c:")
c = int(input())

delta = b**2 - 4*a*c
if delta < 0:
    print("This equation hasn't real roots")
elif delta == 0:
    x = -b/(2*a)
    print("x = {}".format(x))
else:
    x1 = (-b - sqrt(delta))/(a*2)
    x2 = (-b + sqrt(delta))/(a*2)
    print("x1 = {}, x2 = {}".format(x1, x2))

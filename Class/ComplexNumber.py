class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return ComplexNumber(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return ComplexNumber(x, y)

    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + self.y * other.x
        return ComplexNumber(x, y)

    def __truediv__(self, other):
        conj = ComplexNumber(other.x, -other.y)
        den1 = other * conj
        den = den1.x
        nom = self * conj
        return ComplexNumber(nom.x/den, nom.y/den)

    def disp(self):
        print('Complex: {} + i{}'.format(self.x, self.y))


print("Calculator")
print("First complex real part:")
x1 = input()
print("First complex imag part:")
y1 = input()
print("Second complex real part:")
x2 = input()
print("Second complex imag part:")
y2 = input()

com1 = ComplexNumber(x1, y1)
com2 = ComplexNumber(x2, y2)

print('Equation (+-*/):')
eq = input()
if eq == '+':
    ret = com1 + com2
    ret.disp()
elif eq == '-':
    ret = com1 - com2
    ret.disp()
elif eq == '*':
    ret = com1 * com2
    ret.disp()
elif eq == '/':
    ret = com1 / com2
    ret.disp()
else:
    print("Wrong equation!")

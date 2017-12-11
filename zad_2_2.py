import math


class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return '(%s, %s)' % (self.real, self.imag)

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)


if __name__ == '__main__':
    a = Complex(2, 3)
    b = Complex(4, -6)
    print('a = {compa}, b = {compb}, a + b = {add}, a - b = {sub}, abs(a) = {absa}, abs(b) = {absb}'.format(compa=a,
                                                                                                            compb=b,
                                                                                                            add=a + b,
                                                                                                            sub=a - b,
                                                                                                            absa=abs(a),
                                                                                                            absb=abs(
                                                                                                                b)))
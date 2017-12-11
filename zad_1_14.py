import numpy


def wyznacznik(a):
    a = numpy.array(a)
    return numpy.linalg.det(a)


if __name__ == '__main__':
    print(wyznacznik([[1, 2], [3, 4]]))
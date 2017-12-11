import numpy


def suma_macierzy():
    array1 = numpy.random.randint(10, size=(128, 128))
    array2 = numpy.random.randint(10, size=(128, 128))
    return array1 + array2


if __name__ == '__main__':
    print(suma_macierzy())
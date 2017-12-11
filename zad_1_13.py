import numpy


def mnozenie_macierzy():
    a = numpy.random.randint(10, size=(8, 8))
    b = numpy.random.randint(10, size=(8, 8))
    rows__a = len(a)
    cols__a = len(a[0])
    rows__b = len(b)
    cols__b = len(b[0])
    C = [[0 for row in range(cols__b)] for col in range(rows__a)]
    for i in range(rows__a):
        for j in range(cols__b):
            for k in range(cols__a):
                C[i][j] += a[i][k] * b[k][j]
    return C


if __name__ == '__main__':
    print(mnozenie_macierzy()) 
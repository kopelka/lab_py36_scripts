import math


def pierwiastki():
    a = float(input('a:'))
    b = float(input('b:'))
    c = float(input('c:'))
    delta = (b ** 2) - 4 * a * c
    if delta > 0:
        x1 = ((-b) * (- math.sqrt(delta))) / (2 * a)
        x2 = ((-b) * (- math.sqrt(delta))) / (2 * a)
        return x1, x2
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        print('brak pierwiastkow')
        return 0


if __name__ == '__main__':
    print(pierwiastki())
import random
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Lock, Array


def create_list():
    list = []
    for i in range(0, 100):
        list.append(random.randint(0, 39))
    return list


def create_histogram():
    list = [0]*40
    return list


def hist(lista, histogram, lk):
    for l in lista:
        histogram[l] = histogram[l] + 1
    return histogram


if __name__ == '__main__':
    l = Lock()
    pool = Pool(processes=2)
    lista = create_list()
    histogram = create_histogram()
    hist(lista, histogram, l)

    arr = Array('i', range(40))
    for k in range(0, 40):
        arr[k] = 0

    p1 = Process(target=hist, args=(lista[0:50], arr, l))
    p2 = Process(target=hist, args=(lista[50:100], arr, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    for i in range(0, 40):
        if 0 != (arr[i] - histogram[i]):
            print("fail")
    for i in range(0, 40):
        print(arr[i])

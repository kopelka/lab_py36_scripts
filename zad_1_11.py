

def iloczyn_skalany(v1, v2):
    i = 0
    iloczyn = 0
    if len(v1) != len(v2):
        print('wektory musza byc rownej dlugosci')
        return 0
    while i < len(v1):
        iloczyn = iloczyn + v1[1] * v2[i]
        i = i + 1
    return iloczyn


if __name__ == '__main__':
    print(iloczyn_skalany([1, 2, 12, 4], [2, 4, 2, 8]))
import random


def losuj(liczba_el, min_el, max_el):
    tab = []
    while liczba_el:
        tab.append(random.randint(min_el, max_el))
        liczba_el -= 1
    return tab


def sortuj(tab):
    for i in range(len(tab)):
        j = len(tab) - 1
        while j > i:
            if tab[j] > tab[j - 1]:
                tmp = tab[j]
                tab[j] = tab[j - 1]
                tab[j - 1] = tmp
            j -= 1
    return tab


if __name__ == '__main__':
    foo = losuj(50, 1, 100)
    if sortuj(foo) == sorted(foo, reverse=True):
        print('dobrze posortowano tablice')
    else:
        print('cos poszlo nie tak z sortowaniem')
def zapisz_odczytaj(file_name, str_to_write):
    with open(file_name, 'w') as f:
        f.write(str(str_to_write))
    with open(file_name, 'r') as fr:
        odczytane = fr.readline()
        if odczytane == str_to_write:
            return 'ok'
        else:
            return 'zly zapis lub odczyt'


if __name__ == '__main__':
    print(zapisz_odczytaj('plik_testowy.txt', 'str_to_write'))
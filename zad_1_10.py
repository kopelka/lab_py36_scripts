
def zamieniaj_w_pliku(input_file_name):
    pary = {'i': 'oraz', 'oraz': 'i', 'dlaczego': 'czemu', 'nigdy': 'prawie nigdy'}
    i = 0
    with open(input_file_name, 'r') as inputfile:
        with open('output_file_name.txt', 'w') as outputfile:
            for line in inputfile:
                while i < len(pary):
                    line = line.replace(' ' + list(pary)[i] + ' ', ' ' + pary[list(pary)[i]] + ' ')
                    i = i + 1
                outputfile.write(line)
                i = 0


if __name__ == '__main__':
    zamieniaj_w_pliku('przykladowy_tekst.txt')
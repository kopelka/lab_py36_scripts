
def usuwaj_z_pliku(input_file_name):
    slowa = ['i', 'się', 'oraz', 'dlaczego', 'nigdy']
    i = 0
    with open(input_file_name, 'r') as inputfile:
        with open('output_file_name.txt', 'w') as outputfile:
            for line in inputfile:
                while i < len(slowa):
                    line = line.replace(' ' + slowa[i] + ' ', " ")
                    i = i + 1
                outputfile.write(line)
                i = 0


if __name__ == '__main__':
    usuwaj_z_pliku('przykladowy_tekst.txt')
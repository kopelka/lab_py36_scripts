
def check_key(key):
    i = 0
    while i < 3:
        current_key = input('Podaj szyfr (masz 3 proby):')
        i = i + 1
        if str(current_key) == str(key):
            print('ok')
        else:
            print('wrong key')


if __name__ == '__main__':
    check_key('ggg')
import os


def dir_tree(sciezka):
    cnt = 0
    for root, dirs, files in os.walk(sciezka):
        for i in dirs:
            print(i)
            cnt = cnt + 1
    print(cnt)


if __name__ == '__main__':
    dir_tree('D:/Projects/inżynierka/')
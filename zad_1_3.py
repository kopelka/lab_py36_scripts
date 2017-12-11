import os


def dir_count(path):
    counted_dirs = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if root == path:
                print(os.path.join(root, name))
                counted_dirs = counted_dirs + 1

    print(counted_dirs)


if __name__ == '__main__':
    dir_count("./")
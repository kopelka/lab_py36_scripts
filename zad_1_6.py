from PIL import Image


def converting(file_name):
    im = Image.open(file_name + '.jpg')
    im.save(file_name + '.png', 'PNG')


if __name__ == '__main__':
    converting('kotek')
    converting('inny_kotek')
    converting('slodki_kotek')
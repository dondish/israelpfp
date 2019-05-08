from PIL import Image
from os import path
import os


def fetch_israeli_flag():
    return Image.open(path.join(path.dirname(path.realpath(__file__)), "israel.png"))


def handle_picture(ipath, opath):
    im = Image.open(ipath)

    flag = fetch_israeli_flag()

    frames = []

    try:
        while True:
            frame = flag.convert('RGBA').resize(im.size)
            blend = Image.blend(frame, im.convert('RGBA'), 0.85)
            frames.append(blend)
            im.seek(im.tell() + 1)

    except EOFError:
        pass

    frames[0].save(opath, format='GIF', append_images=frames[1:], save_all=True, duration=30, loop=0)


def main():
    handle_picture(os.environ['ipath'], os.environ['opath'])


if __name__ == '__main__':
    main()

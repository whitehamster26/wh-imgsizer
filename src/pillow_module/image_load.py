from PIL import Image

DOESNT_SUPPORT_MESSAGE = "Sorry, this file doesn't support :("


def load_image(file):
    try:
        im = Image.open(file)
        return im, im.size, im.format
    except OSError:
        raise Exception(DOESNT_SUPPORT_MESSAGE)

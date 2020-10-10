import os
from src.pillow_module import image_load

INCORRECT_FORMAT_MESSAGE = "Incorrect input. Please use X-Y format where X is\
 width and Y is height."
INCORRECT_FORMAT_MESSAGE += '\n' + "If you entered a file name or path as an argument, make sure \
that everything is entered correctly."
FILE_NOT_FOUND_MESSAGE = "File not found. Please try again."


def validate_user_input(file, size, name):
    file = file_validator(file)
    size = size_validator(size)
    name = file if not name else name
    return file, size, name


def file_validator(file):
    if os.path.isfile(file):
        return file
    else:
        raise Exception(FILE_NOT_FOUND_MESSAGE)


def size_validator(size):
    if os.path.isfile(size):
        _, size, _ = image_load.load_image(size)
    else:
        size = tuple(filter(lambda x: x.isdecimal(), size.split('-')))
        if len(size) != 2:
            raise Exception(INCORRECT_FORMAT_MESSAGE)
        size = tuple(map(lambda x: int(x), size))
    return size

from .image_load import load_image


def change_size(file_path, size, output_name):
    image_object, image_size, image_format = load_image(file_path)
    resized_image = image_object.resize(size)
    resized_image.save(output_name, format=image_format)

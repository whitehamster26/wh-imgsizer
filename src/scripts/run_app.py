from src.pillow_module import image_process
from src.cli_input_validator import validate_user_input
import click


def show_exceptions(func):
    def func_wrapper():
        try:
            func()
        except Exception as e:
            print('Error:', str(e))
    return func_wrapper


@show_exceptions
@click.command()
@click.argument("file")
@click.argument("size")
@click.option('--name',
              help='Select output filename. By default it rewrites\
 a source file.')
def main(file, size, name):
    file, size, name = validate_user_input(file, size, name)
    image_process.change_size(file, size, name)
    print(f'File {file} was resized to {size[0]}x{size[1]}\
 and saved as {name}.')


if __name__ == "__main__":
    main()

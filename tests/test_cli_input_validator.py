import pytest
from src import cli_input_validator
from tests import TEST_NOT_IMAGE_PATH, TEST_IMAGE_PATH, TEST_IMAGE_SIZE


def test_file_input():
    test_func = cli_input_validator.file_validator
    """ If you put image's path function should return the same path """
    assert test_func('tests/image.jpg') == TEST_IMAGE_PATH
    """ If the file was not found the function raises an error """
    pytest.raises(Exception, test_func, 'image.jpg')


def test_size_input():
    test_func = cli_input_validator.size_validator
    """ A normal input in format W-H should return these numbers in tuple """
    assert test_func('800-600') == (800, 600)
    """ User can print something like WxH or W H and function will raise an error """
    possible_inputs = ('800x600', '800 600', 'foobar', 'foo-bar', '', '\n', '800-600 ')
    for possible_input in possible_inputs:
        pytest.raises(Exception, test_func, possible_input)
    """ Ok here we gonna test if there's file path in size variable. It should return
     file's size (if file is image of course) """
    """ We know that our test image size is (800, 600) so let's test it """
    assert test_func(TEST_IMAGE_PATH) == TEST_IMAGE_SIZE
    """ User can write wrong path to file and we expect an error to be raised """
    pytest.raises(Exception, test_func, 'image.png')
    """ What if file isn't image? Actually it's a problem of another module but we should check it there """
    pytest.raises(Exception, test_func, TEST_NOT_IMAGE_PATH)


def test_validate_user_input():
    test_func = cli_input_validator.validate_user_input
    """ If the user doesn't enter a name, it will be taken from the source file """
    assert test_func(TEST_IMAGE_PATH, "400-400", None) == (TEST_IMAGE_PATH, (400, 400), TEST_IMAGE_PATH)

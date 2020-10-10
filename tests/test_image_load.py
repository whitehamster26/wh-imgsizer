from tests import TEST_IMAGE_PATH, TEST_NOT_IMAGE_PATH, TEST_IMAGE_SIZE, TEST_IMAGE_FORMAT
import pytest
from src.pillow_module.image_load import load_image


def test_image_load():
    """ The function should return the object file, image size, and format """
    assert load_image(TEST_IMAGE_PATH)[1:] == (TEST_IMAGE_SIZE, TEST_IMAGE_FORMAT)
    """ If the file is not an image the function raises an exception  """
    pytest.raises(Exception, load_image, TEST_NOT_IMAGE_PATH)

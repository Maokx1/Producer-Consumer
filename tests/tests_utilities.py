import os
import sys

import cv2
import numpy as np
import pytest

sys.path.insert(0, './')
from src.utilities import config_reader, save_images

sys.path.insert(0, '')


def test_config_reader_empty_path():
    with pytest.raises(TypeError):
        config_reader(section_name='TEST_IMAGE_PROCESSING')


def test_config_reader_empty_section():
    with pytest.raises(TypeError):
        config_reader(config_path='./config_test.cfg')


def test_config_reader_no_file():
    with pytest.raises(SystemExit):
        config_reader(config_path='./s.cfg', section_name='TEST_IMAGE_PROCESSING')


def test_config_reader_no_section():
    with pytest.raises(SystemExit):
        config_reader(config_path='./config_test.cfg', section_name='sadeqwe')


def test_config_reader_no_variable():
    config = config_reader(config_path='./config_test.cfg', section_name='TEST_IMAGE_PROCESSING')
    with pytest.raises(KeyError):
        config['DUTY']


def test_correct_config_reader():
    config = config_reader(config_path='./config_test.cfg', section_name='TEST_IMAGE_PROCESSING')
    assert config['IMAGES_PATH'] == '.'


def test_save_images_empty_queue():
    with pytest.raises(TypeError):
        save_images(path='.')


def test_save_images_empty_path():
    with pytest.raises(TypeError):
        save_images(queue=[np.zeros((10, 10, 2))])


def test_save_images_empty_image():
    with pytest.raises(cv2.error):
        save_images(queue=[np.array([])], path='p')


def test_correct_saving_images():
    save_images(queue=[np.zeros((10, 10, 3))], path='p')
    assert os.path.exists('./p/0.png') is True
    os.remove('./p/0.png')
    os.rmdir('./p')

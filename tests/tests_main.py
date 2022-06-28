import os
import sys

import pytest

sys.path.insert(0, './')
from src.consumer import Consumer
from src.main import image_processing, main
from src.producer import Producer

sys.path.insert(0, '')


def test_image_processing_empty_producer():
    c = Consumer()
    with pytest.raises(TypeError):
        image_processing(c=c, scale_percentage_=50, max_length=10, ksize=5)


def test_image_processing_empty_consumer():
    p = Producer((10, 10, 2))
    with pytest.raises(TypeError):
        image_processing(p=p, scale_percentage_=50, max_length=10, ksize=5)


def test_image_processing_empty_scale():
    c = Consumer()
    p = Producer((10, 10, 2))
    with pytest.raises(TypeError):
        image_processing(c=c, p=p, max_length=10, ksize=5)


def test_image_processing_empty_length():
    c = Consumer()
    p = Producer((10, 10, 2))
    with pytest.raises(TypeError):
        image_processing(c=c, p=p, scale_percentage_=50, ksize=5)


def test_image_processing_empty_ksize():
    c = Consumer()
    p = Producer((10, 10, 2))
    with pytest.raises(TypeError):
        image_processing(c=c, p=p, scale_percentage_=50, max_length=10)


def test_image_processing_empty_producer_queue():
    c = Consumer()
    p = Producer((10, 10, 2))
    image_processing(c=c, p=p, scale_percentage_=50, max_length=10, ksize=5)
    assert len(c.b_queue) == 0


def test_correct_image_processing():
    c = Consumer()
    p = Producer((10, 10, 2))
    p.fill_queue(max_length=10)
    image_processing(c=c, p=p, scale_percentage_=50, max_length=10, ksize=5)
    assert len(c.b_queue) == 1


def test_correct_main():
    main(config_file='./config_test.cfg', section_name='TEST_IMAGE_PROCESSING')
    assert os.path.exists('./0.png') is True
    os.remove('./0.png')

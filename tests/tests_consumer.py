import sys

import cv2
import numpy as np
import pytest

sys.path.insert(0, './')
from src.consumer import Consumer
from src.producer import Producer

sys.path.insert(0, '')


def test_filled_queue():
    c = Consumer()
    c.fill_queue(image=np.zeros((10, 10, 2)), max_length=1)
    c.fill_queue(image=np.zeros((10, 10, 2)), max_length=1)
    assert len(c.b_queue) == 1


def test_unfilled_queue():
    c = Consumer()
    c.fill_queue(image=np.zeros((10, 10, 2)), max_length=5)
    c.fill_queue(image=np.zeros((10, 10, 2)), max_length=5)
    c.fill_queue(image=np.zeros((10, 10, 2)), max_length=5)
    assert len(c.b_queue) == 3


def test_resizing_empty_image_argument():
    with pytest.raises(TypeError):
        c = Consumer()
        c.resize_image(scale_percentage=50)


def test_resizing_empty_image():
    with pytest.raises(IndexError):
        c = Consumer()
        c.resize_image(image=np.array([]), scale_percentage=50)


def test_resizing_empty_scale_argument():
    with pytest.raises(TypeError):
        c = Consumer()
        c.resize_image(image=np.zeros((10, 10, 2)))


def test_resizing_wrong_value_scale():
    with pytest.raises(cv2.error):
        c = Consumer()
        c.resize_image(image=np.zeros((10, 10, 2)), scale_percentage=-1)


def test_correct_image_resizing():
    c = Consumer()
    p = Producer(source_shape=(10, 10, 2))
    p.fill_queue(max_length=1)
    res = c.resize_image(image=p.a_queue[0], scale_percentage=50)
    assert res.shape == (5, 5, 2)


def test_filtering_empty_image_argument():
    with pytest.raises(TypeError):
        c = Consumer()
        c.median_filter(ksize=5)


def test_filtering_empty_ksize_argument():
    with pytest.raises(TypeError):
        c = Consumer()
        c.median_filter(image=np.zeros((10, 10, 2)))


def test_filtering_image_too_small():
    with pytest.raises(cv2.error):
        c = Consumer()
        c.median_filter(image=np.array([]), ksize=5)


def test_filtering_wrong_ksize():
    with pytest.raises(cv2.error):
        c = Consumer()
        c.median_filter(image=np.zeros((10, 10, 2)), ksize=4)


def test_correct_image_filtering():
    c = Consumer()
    p = Producer(source_shape=(10, 10, 2))
    p.fill_queue(max_length=1)
    fil = c.median_filter(image=p.a_queue[0], ksize=5)
    assert fil.shape == (10, 10, 2)

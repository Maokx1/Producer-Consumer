import sys

import pytest

sys.path.insert(0, './')
from src.source import Source

sys.path.insert(0, '')


def test_empty_source_shape():
    with pytest.raises(TypeError):
        Source()


def test_source_shape_wrong_type():
    with pytest.raises(TypeError):
        s = Source(source_shape={1, 3, 2})
        s.get_data()


def test_wrong_size_source_shape():
    with pytest.raises(ValueError):
        s = Source(source_shape=(12, 12))
        s.get_data()


def test_correct_image_size():
    s = Source(source_shape=(10, 10, 2))
    img = s.get_data()
    assert img.shape == (10, 10, 2)

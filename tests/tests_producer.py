import sys

import pytest

sys.path.insert(0, './')
from src.producer import Producer

sys.path.insert(0, '')


def test_empty_source_shape():
    with pytest.raises(TypeError):
        Producer()


def test_filled_queue():
    p = Producer(source_shape=(10, 10, 2))
    p.fill_queue(max_length=1)
    p.fill_queue(max_length=1)
    assert len(p.a_queue) == 1


def test_unfilled_queue():
    p = Producer(source_shape=(10, 10, 2))
    p.fill_queue(max_length=5)
    p.fill_queue(max_length=5)
    p.fill_queue(max_length=5)
    assert len(p.a_queue) == 3

import pytest


def func(x):
    return x + 10


def test_method():
    assert func(3) == 8

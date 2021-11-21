import pytest


def func(x):
    return x + 10


def test_method():
    assert func(3) == 8

def test_policy():
    assert func(4) == 14


def test_cancellation():
    assert func(5) == 15
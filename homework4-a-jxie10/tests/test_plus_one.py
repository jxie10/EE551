import pytest

from mypkg.my_answers import plus_one


def test_example1():
    digits = [1, 2, 3]
    assert([1, 2, 4] == plus_one(digits))


def test_case1():
    digits = [9, 9]
    assert([1, 0, 0] == plus_one(digits))









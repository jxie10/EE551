import pytest

from mypkg.my_answers import roman_to_integers


def test_example1():
    roman_string = "III"
    assert(3 == roman_to_integers(roman_string))


def test_example2():
    roman_string = "IV"
    assert (4 == roman_to_integers(roman_string))


def test_example4():
    roman_string = "LVIII"
    assert (58 == roman_to_integers(roman_string))


def test_example5():
    roman_string = "MCMXCIV"
    assert (1994 == roman_to_integers(roman_string))


def test_case1():
    roman_string = "XC"
    assert (90 == roman_to_integers(roman_string))





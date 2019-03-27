import pytest

from mypkg.my_answers import generateParenthesis


def test_example():
    n = 3
    res = ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert(res == generateParenthesis(n))


def test_case3():
    n = 0
    res = ['']
    assert(res == generateParenthesis(n))
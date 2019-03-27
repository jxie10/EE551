import pytest

from mypkg.my_answers import isPalindrome

def test_example1():
    s = "A man, a plan, a canal: Panama"
    assert(isPalindrome(s))


def test_case3():
    s = "Sir, I demand, I am a maid named Iris"
    assert(isPalindrome(s))







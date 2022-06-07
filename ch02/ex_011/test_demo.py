import pytest


def div(a,b):
    return a/b

def test_demo01():
    pytest.raises(ZeroDivisionError,div,10,0)

def test_demo02():
    pytest.raises(ZeroDivisionError,div,10,5)
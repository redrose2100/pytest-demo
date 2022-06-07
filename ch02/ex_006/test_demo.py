import pytest


def div(a,b):
    return a/b

def test_demo():
    with pytest.raises(ZeroDivisionError):
        c=div(10,0)
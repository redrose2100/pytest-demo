import pytest


def div(a,b):
    return a/b

def test_demo():
    with pytest.raises(ZeroDivisionError,match=r"division\s*by\s*zero"):
        c=div(10,0)


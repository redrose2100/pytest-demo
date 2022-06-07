import pytest


def div(a,b):
    return a/b

def test_demo():
    with pytest.raises(ZeroDivisionError) as e:
        c=div(10,0)

    assert "division by zero" in str(e.value)
import pytest

def sum(x,y):
    return x+y

def test_sum_01():
    assert sum(1,2) == 3

if __name__=="__main__":
    pytest.main(["test_sum.py"])
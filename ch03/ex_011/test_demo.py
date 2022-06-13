
def setup_function():
    print("in setup_function ...")

def teardown_function():
    print("in teardown_function ...")

def test_01():
    print("in test_01 ...")
    assert 1==1

def test_02():
    print("in test_02 ...")
    assert 1==1
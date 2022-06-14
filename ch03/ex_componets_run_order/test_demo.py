

class TestDemo(object):
    def setup_class(self):
        print("in TestDemo.setup_class ...")

    def teardown_class(self):
        print("in TestDemo.teardown_class ...")

    def setup_method(self):
        print("in TestDemo.setup_method ...")

    def teardown_method(self):
        print("in TestDemo.teardown_method ...")

    def test_03(self):
        print("in TestDemo.test_03 ...")
        assert 1==1

    def test_04(self):
        print("in TestDemo.test_04 ...")
        assert 1==1

def setup_module():
    print("in setup_module ...")

def teardown_module():
    print("in teardown_module ...")

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
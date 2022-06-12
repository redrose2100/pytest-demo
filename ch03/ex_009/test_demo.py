
class TestDemo(object):
    def setup_method(self):
        print("in setup_method ...")

    def teardown_method(self):
        print("in teardown_method ...")

    def test_01(self):
        print("in test_01 ...")
        assert 1==1

    def test_02(self):
        print("in test_02 ...")
        assert 1==1


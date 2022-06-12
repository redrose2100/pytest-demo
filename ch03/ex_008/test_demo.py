
class TestDemo(object):
    def setup_class(self):
        print("in setup_class ...")

    def teardown_class(self):
        print("in teardown_class ...")

    def test_01(self):
        print("in test_01 ...")
        assert 1==1

    def test_02(self):
        print("in test_02 ...")
        assert 1==1


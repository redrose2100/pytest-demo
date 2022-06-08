
class Company(object):
    def __init__(self,sale):
        self.sale=sale

    def __eq__(self,other):
        return self.sale == other.sale


def test_demo():
    c1=Company(100)
    c2=Company(10000)
    assert c1==c2
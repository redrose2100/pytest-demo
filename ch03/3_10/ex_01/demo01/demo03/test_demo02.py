import sys

print("sys.path:%s" % sys.path)
for elem in sys.modules.keys():
    if "demo" in elem:
        print("module:"+elem)

def test_func():
    assert 1==1
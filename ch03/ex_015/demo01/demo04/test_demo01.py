import sys

print("in test_demo02 ...")
for elem in sys.path:
    if "pytest-demo" in elem:
        print("sys.path:" + elem)
for elem in sys.modules.keys():
    if "demo" in elem:
        print("module:"+elem)

def test_func():
    assert 1==1
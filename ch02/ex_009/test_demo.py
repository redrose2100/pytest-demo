
def div(a,b):
    return a/b

def test_demo():
    try:
        c=div(10,0)
    except Exception as e:
        assert isinstance(e, ZeroDivisionError)
        assert "division by zero" in str(e)
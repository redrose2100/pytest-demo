def test_01():
    assert 1==1
def test_02():
    assert 1==2
def test_03():
    assert "1"==1
def test_04():
    assert "aa" in "bbaa"
def test_05():
    assert "aa" in "bba"
def test_06():
    assert "aa" in ["aa","bb"]
def test_07():
    assert "aa" in ("aa","bb")
def test_08():
    assert "aa" in {"aa","bb"}
def test_09():
    assert "ab" in ["aa", "bb"]
def test_10():
    assert "ab" in ("aa", "bb")
def test_11():
    assert "ab" in {"aa", "bb"}
def test_12():
    assert "name" in {"name":"张三丰","age":100}
def test_13():
    assert "gender" in {"name":"张三丰","age":100}
def test_14():
    assert "aa" not in "bbaa"
def test_15():
    assert "aa" not in "bba"
def test_16():
    assert "aa" not in ["aa","bb"]
def test_17():
    assert "aa" not in ("aa","bb")
def test_18():
    assert "aa" not in {"aa","bb"}
def test_19():
    assert "ab" not in ["aa", "bb"]
def test_20():
    assert "ab" not in ("aa", "bb")
def test_21():
    assert "ab" not in {"aa", "bb"}
def test_22():
    assert "name" not in {"name":"张三丰","age":100}
def test_23():
    assert "gender" not in {"name":"张三丰","age":100}

def pytest_assertrepr_compare(op, left, right):
    if op == "==":
        if not isinstance(right,type(left)):
            return [
                f"断言错误，期望值与实际值的数据类型不一致，期望值数据类型为：{type(right)}， 实际值为：{type(left)}",
                f"期望值为：{right}， 实际值为：{left}",
            ]
        else:
            return [
                f"断言错误，期望值与实际值不一致，期望值为：{right}， 实际值为：{left}",
            ]
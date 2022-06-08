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
    if op == "in":
        if isinstance(left,str) and isinstance(right,str):
            return [
                f"期望 {left} 是 {right} 的子串，实际 {left} 不是 {right} 的子串,"
            ]
        elif isinstance(right,list) or isinstance(right,set) or isinstance(right,tuple):
            return [
                f"期望 {left} 是集合 {right} 中的一个元素，实际集合 {right} 中没有 {left} 元素"
            ]
        elif isinstance(right,dict):
            return [
                f"期望 {left} 是字典 {right} 中的一个key，实际字典 {right} 中没有值为 {left} 的key"
            ]
        else:
            return [
                f"期望 {left} 是 {right} 中的一部分，实际上 {left} 并不是 {right} 的一部分"
            ]
    if op == "not in":
        if isinstance(left, str) and isinstance(right, str):
            return [
                f"期望 {left} 不是 {right} 的子串，实际 {left} 是 {right} 的子串,"
            ]
        elif isinstance(right, list) or isinstance(right, set) or isinstance(right, tuple):
            return [
                f"期望 {left} 不是集合 {right} 中的一个元素，实际集合 {right} 中有 {left} 元素"
            ]
        elif isinstance(right, dict):
            return [
                f"期望 {left} 不是字典 {right} 中的一个key，实际字典{right}中有值为 {left} 的key"
            ]
        else:
            return [
                f"期望 {left} 不是 {right} 中的一部分，实际上 {left} 是 {right} 的一部分"
            ]
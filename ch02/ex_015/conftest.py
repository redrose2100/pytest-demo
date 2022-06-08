from .test_demo import Company

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Company) and isinstance(right, Company) and op == "==":
        return [
            "两个公司销售额不相等，他们的销售额分别是:",
            "销售额: {} != {}".format(left.sale, right.sale),
        ]
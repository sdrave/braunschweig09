from bisec import bisec

def test_result():
    f = lambda x: x
    x = bisec(f, -1, 1)
    assert abs(x) < 1e-4

def test_result2():
    f = lambda x: x
    x = bisec(f, -2, 1)
    assert abs(x) < 1e-4

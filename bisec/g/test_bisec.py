import pytest
from bisec import bisec

def test_result():
    f = lambda x: x
    x = bisec(f, -1, 1)
    assert abs(x) < 1e-4

def test_result2():
    f = lambda x: x
    x = bisec(f, -2, 1)
    assert abs(x) < 1e-4

def test_minus_plus():
    f = lambda x: x**3 - 1
    x = bisec(f, -2, 1.5)
    assert abs(x) < 1e-4

def test_plus_minus():
    f = lambda x: -x**3 + 1
    x = bisec(f, -2, 1.5)
    assert abs(x) < 1e-4

def test_no_zero():
    f = lambda x: x**2 + 1
    with pytest.raises(ValueError):
        x = bisec(f, -2, 1.5)

def test_zero_left():
    f = lambda x: x**2
    x = bisec(f, 0, 1)
    assert abs(x) < 1e-4

def test_zero_right():
    f = lambda x: x**2
    x = bisec(f, -1, 0)
    assert abs(x) < 1e-4

def test_discont():
    f = lambda x: -1 if x < 0 else 1
    with pytest.raises(ValueError):
        x = bisec(f, -2, 1.5)

def test_a_equal_b():
    f = lambda x: x**2 - 1
    with pytest.raises(ValueError):
        x = bisec(f, -2, -2)

def test_a_equal_b_equal_root():
    f = lambda x: x**2 - 1
    x = bisec(f, -1, -1)
    assert abs(x) < 1e-4

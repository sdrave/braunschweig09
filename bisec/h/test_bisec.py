import pytest
from bisec import bisec

@pytest.fixture(params=[1, 1e-2, 1e-3, 1e-4, 1e-7])
def tol(request):
    return request.param


def test_result(tol):
    f = lambda x: x
    x = bisec(f, -1, 1, tol=tol)
    assert abs(x) < tol

def test_result2(tol):
    f = lambda x: x
    x = bisec(f, -2, 1, tol=tol)
    assert abs(x) < tol

def test_minus_plus(tol):
    f = lambda x: x**3 - 1
    x = bisec(f, -2, 1.5, tol=tol)
    assert abs(x) < tol

def test_plus_minus(tol):
    f = lambda x: -x**3 + 1
    x = bisec(f, -2, 1.5, tol=tol)
    assert abs(x) < tol

def test_no_zero(tol):
    f = lambda x: x**2 + 1
    with pytest.raises(ValueError):
        x = bisec(f, -2, 1.5, tol=tol)

def test_zero_left(tol):
    f = lambda x: x**2
    x = bisec(f, 0, 1, tol=tol)
    assert abs(x) < tol

def test_zero_right(tol):
    f = lambda x: x**2
    x = bisec(f, -1, 0, tol=tol)
    assert abs(x) < tol

def test_discont(tol):
    f = lambda x: -1 if x < 0 else 1
    with pytest.raises(ValueError):
        x = bisec(f, -2, 1.5, tol=tol)

def test_a_equal_b(tol):
    f = lambda x: x**2 - 1
    with pytest.raises(ValueError):
        x = bisec(f, -2, -2, tol=tol)

def test_a_equal_b_equal_root(tol):
    f = lambda x: x**2 - 1
    x = bisec(f, -1, -1, tol=tol)
    assert abs(x) < tol

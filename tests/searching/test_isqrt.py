import math
import pytest
from dsa.searching.isqrt import isqrt


def test_small():
    for n, expected in enumerate([0, 1, 1, 1, 2, 2, 2, 2, 2, 3]):
        assert isqrt(n) == expected


def test_negative():
    with pytest.raises(ValueError):
        isqrt(-1)


@pytest.mark.parametrize("n", [
    0, 1, 2, 3, 4, 5, 8, 9, 10, 15, 16, 17,
    99, 100, 101, 10**6, 10**6 - 1, (10**6) ** 2, (10**6) ** 2 - 1,
    10**18, 10**18 - 1,
])
def test_against_math_isqrt(n):
    assert isqrt(n) == math.isqrt(n)


def test_boundary_squares():
    """Особенно ловит off-by-one: r*r == n и r*r == n-1."""
    for r in range(1, 1000):
        assert isqrt(r * r) == r
        assert isqrt(r * r - 1) == r - 1
        assert isqrt(r * r + 1) == r
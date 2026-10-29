import bisect
import random
import pytest
from dsa.searching.binary_search import binary_search
from dsa.searching.linear_search import linear_search


def test_empty():
    assert binary_search([], 5) == -1


def test_single():
    assert binary_search([7], 7) == 0
    assert binary_search([7], 5) == -1


def test_found():
    a = [1, 3, 5, 7, 9, 11]
    assert binary_search(a, 1) == 0
    assert binary_search(a, 5) == 2
    assert binary_search(a, 11) == 5
    assert binary_search(a, 4) == -1
    assert binary_search(a, 0) == -1
    assert binary_search(a, 100) == -1


def test_range():
    a = [1, 3, 5, 7, 9, 11]
    # индексы: 0  1  2  3  4  5
    assert binary_search(a, 5, lo=2) == 2
    assert binary_search(a, 1, lo=1) == -1          # 1 левее lo
    assert binary_search(a, 9, hi=4) == -1          # 9 на индексе 4, не включён
    assert binary_search(a, 7, lo=1, hi=4) == 3


def test_range_clamps():
    a = [1, 2, 3]
    assert binary_search(a, 1, lo=-5) == 0
    assert binary_search(a, 3, hi=100) == 2
    assert binary_search(a, 2, lo=10) == -1
    assert binary_search(a, 2, lo=2, hi=1) == -1


@pytest.mark.parametrize("seed", range(50))
def test_against_bisect(seed):
    """Эталон — bisect.bisect_left. На массиве с дубликатами
    binary_search может вернуть любой из совпадающих индексов,
    поэтому проверяем 'a[результат] == x' или '-1', если x нет."""
    random.seed(seed)
    n = random.randint(0, 200)
    a = sorted(random.randint(-50, 50) for _ in range(n))
    for x in range(-55, 55):
        r = binary_search(a, x)
        present = x in a
        if present:
            assert r != -1
            assert a[r] == x
        else:
            assert r == -1


@pytest.mark.parametrize("seed", range(20))
def test_binary_matches_linear(seed):
    """binary_search и linear_search должны согласовываться
    по контракту: одинаково находить/не находить."""
    random.seed(seed)
    a = sorted(random.randint(0, 9) for _ in range(100))
    for x in range(10):
        r_bin = binary_search(a, x)
        r_lin = linear_search(a, x)
        assert (r_bin == -1) == (r_lin == -1)
        if r_bin != -1:
            assert a[r_bin] == x

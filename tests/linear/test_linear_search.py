import pytest
from dsa.searching.linear_search import linear_search


def test_empty():
    assert linear_search([], 5) == -1


def test_single():
    assert linear_search([7], 7) == 0
    assert linear_search([7], 5) == -1


def test_basic():
    a = [3, 1, 4, 1, 5, 9, 2, 6]
    assert linear_search(a, 4) == 2
    assert linear_search(a, 1) == 1
    assert linear_search(a, 9) == 5
    assert linear_search(a, 42) == -1


def test_range():
    a = [1, 2, 1, 2, 1]
    assert linear_search(a, 1) == 0
    assert linear_search(a, 1, start=1) == 2
    assert linear_search(a, 1, start=3) == 4
    assert linear_search(a, 1, start=5) == -1
    assert linear_search(a, 2, stop=3) == 1
    assert linear_search(a, 1, start=2, stop=3) == 2


def test_range_clamps():
    a = [1, 2, 3]
    assert linear_search(a, 1, start=-5) == 0
    assert linear_search(a, 3, stop=100) == 2


@pytest.mark.parametrize("seed", range(20))
def test_against_list_index(seed):
    import random
    random.seed(seed)
    a = [random.randint(0, 9) for _ in range(100)]
    for x in range(10):
        try:
            expected = a.index(x)
        except ValueError:
            expected = -1
        assert linear_search(a, x) == expected

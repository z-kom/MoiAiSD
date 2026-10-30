import bisect
import random
import pytest
from dsa.searching.bounds import lower_bound, upper_bound, count_by_bounds


def test_hand_examples():
    a = [1, 3, 3, 3, 5]
    assert lower_bound(a, 3) == 1
    assert upper_bound(a, 3) == 4
    assert upper_bound(a, 3) - lower_bound(a, 3) == 3   # число вхождений

    assert lower_bound(a, 2) == 1
    assert upper_bound(a, 2) == 1

    assert lower_bound(a, 0) == 0
    assert upper_bound(a, 0) == 0

    assert lower_bound(a, 9) == 5
    assert upper_bound(a, 9) == 5


def test_empty_and_single():
    assert lower_bound([], 5) == 0
    assert upper_bound([], 5) == 0
    assert lower_bound([7], 5) == 0
    assert lower_bound([7], 7) == 0
    assert lower_bound([7], 9) == 1
    assert upper_bound([7], 7) == 1


def test_range():
    a = [1, 3, 3, 3, 5]
    assert lower_bound(a, 3, lo=2) == 2
    assert upper_bound(a, 3, hi=3) == 3
    assert lower_bound(a, 1, lo=1) == 1   # первый >= 1 начиная с 1


def test_all_equal():
    a = [5, 5, 5, 5]
    assert lower_bound(a, 5) == 0
    assert upper_bound(a, 5) == 4
    assert lower_bound(a, 4) == 0
    assert lower_bound(a, 6) == 4


@pytest.mark.parametrize("seed", range(50))
def test_against_bisect(seed):
    random.seed(seed)
    n = random.randint(0, 200)
    a = sorted(random.randint(-50, 50) for _ in range(n))
    for x in range(-55, 55):
        assert lower_bound(a, x) == bisect.bisect_left(a, x)
        assert upper_bound(a, x) == bisect.bisect_right(a, x)


def test_x_not_in_array():
    a = [1, 3, 5]
    assert lower_bound(a, 2) == 1
    assert upper_bound(a, 2) == 1
    assert lower_bound(a, 0) == 0
    assert upper_bound(a, 9) == 3
    assert count_by_bounds(a, 2) == 0


def test_upper_is_not_last_occurrence():
    a = [1, 3, 3, 3, 5]
    assert lower_bound(a, 3) == 1
    assert upper_bound(a, 3) == 4
    assert count_by_bounds(a, 3) == 3

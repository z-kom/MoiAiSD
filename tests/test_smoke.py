"""Smoke-тест: проверяет, что каркас собран и хелперы работают."""
from tests.helpers import (
    all_array_kinds,
    almost_sorted_array,
    array_with_duplicates,
    random_array,
    reversed_array,
    sorted_array,
    timer,
)


def test_generators_length():
    assert len(random_array(100)) == 100
    assert len(sorted_array(50)) == 50
    assert len(reversed_array(50)) == 50
    assert len(array_with_duplicates(1000, distinct=5)) == 1000
    assert len(almost_sorted_array(100, swaps=3)) == 100


def test_generators_properties():
    a = sorted_array(50)
    assert a == sorted(a)

    b = reversed_array(50)
    assert b == sorted(b, reverse=True)

    c = array_with_duplicates(5000, distinct=3)
    assert len(set(c)) <= 3


def test_all_array_kinds():
    kinds = all_array_kinds(200)
    assert set(kinds) == {"random", "sorted", "reversed", "duplicates", "almost_sorted"}
    assert all(len(v) == 200 for v in kinds.values())


def test_timer_measures_positive_time():
    with timer() as t:
        sum(range(1000))
    assert t.elapsed > 0

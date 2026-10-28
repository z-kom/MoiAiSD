"""Хелперы для тестов и бенчмарков.

Здесь разрешено использовать встроенные функции (sorted, random, time):
правило «только свои структуры» действует на пакет dsa/, но не на тесты.
"""
from __future__ import annotations

import random
import time
from contextlib import contextmanager


def random_array(n: int, lo: int = -1000, hi: int = 1000) -> list[int]:
    """n случайных целых в [lo, hi]."""
    return [random.randint(lo, hi) for _ in range(n)]


def sorted_array(n: int, lo: int = -1000, hi: int = 1000) -> list[int]:
    return sorted(random_array(n, lo, hi))


def reversed_array(n: int, lo: int = -1000, hi: int = 1000) -> list[int]:
    return sorted(random_array(n, lo, hi), reverse=True)


def array_with_duplicates(n: int, distinct: int = 5) -> list[int]:
    """n элементов, но различных значений ровно distinct (много дубликатов)."""
    pool = random_array(distinct)
    return [random.choice(pool) for _ in range(n)]


def almost_sorted_array(n: int, swaps: int = 3) -> list[int]:
    """Отсортированный массив с swaps случайными перестановками пар."""
    a = sorted_array(n)
    for _ in range(swaps):
        i, j = random.randrange(n), random.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a


def all_array_kinds(n: int) -> dict[str, list[int]]:
    """Удобно для параметризации тестов сортировок:
    все характерные входы в одном словаре."""
    return {
        "random": random_array(n),
        "sorted": sorted_array(n),
        "reversed": reversed_array(n),
        "duplicates": array_with_duplicates(n),
        "almost_sorted": almost_sorted_array(n),
    }


@contextmanager
def timer():
    """Замер времени блока: with timer() as t: ...; print(t.elapsed)."""
    class _T:
        elapsed: float = 0.0

    t = _T()
    start = time.perf_counter()
    try:
        yield t
    finally:
        t.elapsed = time.perf_counter() - start
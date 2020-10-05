"""Тест set"""

import random
import pytest


@pytest.fixture(autouse=True, scope='function')
def random_set():
    """Фикстура, возвращающая множество с 5 случайными числами от 1 до 1000"""
    while True:
        list_a = [random.randint(1, 1000) for i in range(5)]
        get_set = {i for i in list_a}
        if len(get_set) == 5:
            break
    yield get_set


@pytest.mark.parametrize('new_set', [{2, 3, 5}, {1}, {}, {1, 3, 5, 8, 7, 4, 6}])
def test_pop(new_set):
    """Проверка метода clear"""
    length = len(new_set)
    try:
        new_set.pop()
        assert len(new_set) + 1 == length
    except TypeError:
        assert len(new_set) == 0


def test_clear(random_set):
    """Проверка метода clear"""
    random_set.clear()
    assert len(random_set) == 0


class TestClass:
    """Тестовый класс для проверки методов union, intersection и symmetric_difference"""

    first_set = {1, 3 ,5 ,0}
    second_set = {0, 1, 2, 7, 6}

    def test_union(self):
        """Проверка объединения множеств"""
        assert self.first_set.union(self.second_set) == {0, 1, 2, 3, 6, 7, 5}

    def test_intersection(self):
        """Проверка пересечения множеств"""
        assert self.first_set.intersection(self.second_set) == {0, 1}

    def test_sym_difference(self):
        """Проверка выборки уникальных значений из каждого множества"""
        assert self.first_set.symmetric_difference(self.second_set) == {3, 5, 2, 6, 7}

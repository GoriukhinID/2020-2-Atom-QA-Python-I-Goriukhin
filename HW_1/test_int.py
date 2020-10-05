"""Тест int"""

import random
import pytest


@pytest.fixture(autouse=True, scope='session')
def value():
    """Фикстура, возвращающая случайное число от 1 до 100"""
    yield random.randint(1, 100)


@pytest.mark.parametrize('i', [2, 0, -1, 2147483647])
def test_multiply(i, value):
    """Проверка умножения int"""

    multpl_result = sum([i for x in range(value)])
    if i == 2147483647:
        assert multpl_result > i               # Проверяем не произошло ли переполнение
        assert isinstance(multpl_result, int)  # Проверяем не изменился ли тип данных
    else:
        assert i * value == multpl_result


class TestClass:
    """Класс с тестами на сложение и вычитание"""
    pos = 3     # pos > 0
    neg = -1    # neg < 0

    # Проверка сложения int
    def test_add(self, value):
        """Проверка сложения int"""
        assert int(value) + 0 == int(value)

        assert int(value + self.pos) == int(value) + int(self.pos)

        assert int(value + self.neg) == int(value) + int(self.neg)
        print("test_add complete")

    def test_subtract(self, value):
        """Проверка вычитания int"""
        assert int(value) - 0 == int(value)

        assert int(value - self.pos) == int(value) - int(self.pos)

        assert int(value - self.neg) == int(value) - int(self.neg)


def test_division(value):
    """Проверка деления числа типа int"""
    with pytest.raises(ZeroDivisionError):
        value / 0
    with pytest.raises(ZeroDivisionError):
        0 / 0

    assert value / value == 1

    assert 2.33333 < int(7) / int(3) < 2.33334


def test_negation(value):
    """Проверка смены знака у int-переменной"""
    assert value * -1 == -value

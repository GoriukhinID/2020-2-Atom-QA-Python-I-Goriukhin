"""Тест list"""
import random
import pytest


@pytest.fixture(autouse=True, scope='function')
def rand_list_of_3():
    """Фикстура, возвращающая список размера 3 с тремя случайными числами"""
    yield [random.randint(1, 100) for i in range(3)]


def test_len(rand_list_of_3):
    """Проверка определения длины списка"""
    assert len(rand_list_of_3) == 3

    assert len([]) == 0

    appended_list = rand_list_of_3
    appended_list.append(3)
    assert len(appended_list) == 4


class TestClass:
    """Тестовый класс для проверки работы индексов и метода append списка"""
    new_list = [3, "foo", 5.0, True]
    new_list_to_append = [3, "foo", 5.0, True]

    @pytest.mark.parametrize('i', [2, 0, -1, 7])
    def test_index(self,i):
        """Проверка работы индексов списка"""
        if i >= len(self.new_list):
            with pytest.raises(IndexError):
                assert self.new_list[i]
        else:
            assert self.new_list[i]

    def test_append(self):
        """Проверка метода append"""
        self.new_list_to_append.append(42)
        assert len(self.new_list_to_append) == 5
        assert self.new_list_to_append[4] == 42


def test_clear(rand_list_of_3):
    """Проверка метода clear"""
    list_to_clear = rand_list_of_3
    list_to_clear.clear()
    assert len(list_to_clear) == 0


def test_join(rand_list_of_3):
    """Проверка конвертации списка в строку методом join"""
    string = " ".join(map(str, rand_list_of_3))
    assert type(string) == str

"""Test dictionary"""

import pytest


@pytest.fixture(autouse=True, scope='function')
def test_dict():
    """Фикстура c определённым словарём"""
    yield {1: 5, "foo": True, 8: [2, 4],
           42: "Answer to the Ultimate Question of Life, the Universe, and Everything"}


@pytest.mark.parametrize('i', [{2: "full", 3: True, 5: 0}, {1: None}, {}])
def test_clear(i):
    """Проверка метода clear"""
    i.clear()
    assert len(i) == 0


def test_keys(test_dict):
    """Проверка возврата ключей словаря"""
    testing_list = [1, "foo", 8, 42]
    for i in testing_list:
        assert i in test_dict.keys()


def test_values(test_dict):
    """Проверка возврата значений словаря"""
    testing_list = [5, True, [2, 4],
                    "Answer to the Ultimate Question of Life, the Universe, and Everything"]
    for i in testing_list:
        assert i in test_dict.values()


class TestClass:
    """Класс для проверки метода items"""
    class_dict = {2: 3, "test": "items", 5: None}
    keys = [2, "test", 5]
    values = [3, "items", None]

    def test_items(self):
        """Проверка возврата ключей и значений словаря"""
        for key, value in self.class_dict.items():
            assert key in self.keys
            assert value in self.values


def test_update(test_dict):
    """Проверка метода update"""
    old_length = len(test_dict)
    test_dict.update({5: "new_value"})
    assert len(test_dict) == old_length + 1
    assert test_dict[5] == "new_value"

    old_length = len(test_dict)
    test_dict.update({1: "some"})
    assert len(test_dict) == old_length
    assert test_dict[1] == "some"

"""Test string"""

import pytest


@pytest.fixture(autouse=True, scope='function')
def new_str():
    """Фикстура c определённым словарём"""
    yield "Testing string"


def test_split(new_str):
    """Проверка метода split"""
    assert new_str.split(' ') == ["Testing", "string"]


@pytest.mark.parametrize('string', ["some_stroke", "", "12345", "QA-2020"])
def test_isdigit(string):
    """Проверка метода isdigit"""
    if string == "12345":
        assert string.isdigit()
    else:
        assert not string.isdigit()


class TestClass:
    """Тестовый класс"""
    list_with_str = ["some", "", "12345", "QA-2020"]

    def test_isalpha(self):
        for i in self.list_with_str:
            if i == "some":
                assert i.isalpha()
            else:
                assert not i.isalpha()

    def test_islower(self):
        for i in self.list_with_str:
            if i == "some":
                assert i.islower()
            else:
                assert not i.islower()


def test_viil(new_str):
    """Проверка создания среза"""
    assert new_str[8:] == "string"

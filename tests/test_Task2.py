from testshw.Task2 import set_
import pytest


@pytest.fixture
def coll():
    coll = {"a": {"b": {"c": 3}}}
    return coll


def test_set_1(coll):
    assert set_(coll, ["a", "b", "c"], 4) == {"a": {"b": {"c": 4}}}


def test_set_2(coll):
    assert set_(coll, ["x", "y", "z"], 5) == {'a': {'b': {'c': 3}}, 'x': {'y': {'z': 5}}}

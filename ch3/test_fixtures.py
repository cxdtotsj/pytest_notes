# fixture 入门

import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    """Use fixture return value in a test."""

    assert some_data == 42


# fixture 存放数据
@pytest.fixture()
def a_tuple():
    return (1, 'foo', None, {'bar': 23})

def test_a_tuple(a_tuple):
    assert a_tuple[3]['bar'] == 32

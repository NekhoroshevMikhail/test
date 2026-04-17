import pytest
from main import sort_values

def test_sort_basic():
    values = ["green", "red", "blue"]
    order_rule = {"red": "0", "blue": "1", "green": "2"}

    result = sort_values(values, order_rule)

    assert result == ["red", "blue", "green"]


def test_sort_with_duplicates():
    values = ["green", "red", "red", "blue"]
    order_rule = {"red": "0", "blue": "1", "green": "2"}

    result = sort_values(values, order_rule)

    assert result == ["red", "red", "blue", "green"]


def test_sort_empty_values():
    values = []
    order_rule = {"red": "0"}

    result = sort_values(values, order_rule)

    assert result == []


def test_sort_single_value():
    values = ["blue"]
    order_rule = {"blue": "1"}

    result = sort_values(values, order_rule)

    assert result == ["blue"]

def test_missing_color_in_order_rule():
    values = ["red"]
    order_rule = {}

    with pytest.raises(KeyError):
        sort_values(values, order_rule)
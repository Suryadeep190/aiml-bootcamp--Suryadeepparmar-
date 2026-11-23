from functional_utils import (
    calculate_product,
    calculate_running_totals,
    calculate_total_price,
    create_word_length_dict,
    filter_long_words,
    flatten_lists,
    multiply_pairs,
    normalize_names,
    remove_falsy_values,
    square_odd_numbers,
)


# TASK 01
def test_square_odd_numbers():
    assert square_odd_numbers([1, 2, 3, 4, 5]) == [1, 9, 25]


def test_square_odd_numbers_empty():
    assert square_odd_numbers([]) == []


# TASK 02
def test_normalize_names():
    assert normalize_names([" alice ", "BOB"]) == ["ALICE", "BOB"]


def test_normalize_names_empty():
    assert normalize_names([]) == []


# TASK 03
def test_multiply_pairs():
    assert multiply_pairs([2, 3, 4], [5, 6, 7]) == [10, 18, 28]


def test_multiply_pairs_empty():
    assert multiply_pairs([], []) == []


def test_multiply_pairs_unequal_lengths():
    import pytest

    with pytest.raises(ValueError):
        multiply_pairs([2, 3], [4])


# TASK 04
def test_filter_long_words():
    assert filter_long_words(["cat", "apple", "dog", "banana"]) == [
        "apple",
        "banana",
    ]


def test_filter_long_words_empty():
    assert filter_long_words([]) == []


# TASK 05
def test_calculate_product():
    assert calculate_product([2, 3, 4]) == 24


def test_calculate_product_empty():
    assert calculate_product([]) == 1


# TASK 06
def test_calculate_total_price():
    items = [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 1000},
    ]
    assert calculate_total_price(items) == 51000


def test_calculate_total_price_empty():
    assert calculate_total_price([]) == 0


# TASK 07
def test_flatten_lists():
    assert flatten_lists([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_flatten_lists_empty():
    assert flatten_lists([]) == []


# TASK 08
def test_create_word_length_dict():
    assert create_word_length_dict(["apple", "banana", "cat"]) == {
        "apple": 5,
        "banana": 6,
        "cat": 3,
    }


def test_create_word_length_dict_empty():
    assert create_word_length_dict([]) == {}


# TASK 09
def test_remove_falsy_values():
    assert remove_falsy_values([0, 10, "", "Hello", None, [], 25]) == [
        10,
        "Hello",
        25,
    ]


def test_remove_falsy_values_empty():
    assert remove_falsy_values([]) == []


# TASK 10
def test_calculate_running_totals():
    assert calculate_running_totals([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_calculate_running_totals_empty():
    assert calculate_running_totals([]) == []

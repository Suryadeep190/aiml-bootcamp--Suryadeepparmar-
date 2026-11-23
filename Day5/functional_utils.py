"""
Reusable utility functions for functional programming operations.
"""

from functools import reduce
from itertools import accumulate, chain
from typing import TypedDict, TypeVar

T = TypeVar("T")


class Item(TypedDict):
    """Represent an item with a name and price."""

    name: str
    price: int


def square_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Return the squares of all odd numbers.

    Args:
        numbers: A list of integers.

    Returns:
        A list containing the squares of odd numbers.
    """
    return list(map(lambda n: n**2, filter(lambda n: n % 2 != 0, numbers)))


def normalize_names(names: list[str]) -> list[str]:
    """
    Remove surrounding whitespace and convert names to uppercase.

    Args:
        names: A list of names.

    Returns:
        A list of normalized names.
    """
    return list(map(lambda name: name.strip().upper(), names))


def multiply_pairs(numbers1: list[int], numbers2: list[int]) -> list[int]:
    """
    Multiply corresponding elements from two lists.

    Args:
        numbers1: The first list of integers.
        numbers2: The second list of integers.

    Returns:
        A list containing the products of corresponding elements.

    Raises:
        ValueError: If the lists have different lengths.
    """
    if len(numbers1) != len(numbers2):
        raise ValueError("Both lists must have equal lengths.")

    return list(map(lambda pair: pair[0] * pair[1], zip(numbers1, numbers2)))


def filter_long_words(words: list[str]) -> list[str]:
    """
    Return words containing more than three characters.

    Args:
        words: A list of strings.

    Returns:
        A list containing words longer than three characters.
    """
    return list(filter(lambda word: len(word) > 3, words))


def calculate_product(numbers: list[int]) -> int:
    """
    Calculate the product of all numbers in a list.

    Args:
        numbers: A list of integers.

    Returns:
        The product of all numbers. Returns 1 for an empty list.
    """
    return reduce(lambda x, y: x * y, numbers, 1)


def calculate_total_price(items: list[Item]) -> int:
    """
    Calculate the total price of all items.

    Args:
        items: A list of items containing names and prices.

    Returns:
        The sum of all item prices.
    """
    return sum(map(lambda item: item["price"], items))


def flatten_lists(nested_list: list[list[int]]) -> list[int]:
    """
    Convert a nested list into a single flat list.

    Args:
        nested_list: A list containing multiple integer lists.

    Returns:
        A single list containing all the elements.
    """
    return list(chain.from_iterable(nested_list))


def create_word_length_dict(words: list[str]) -> dict[str, int]:
    """
    Create a dictionary containing words and their lengths.

    Args:
        words: A list of strings.

    Returns:
        A dictionary mapping each word to its length.
    """
    return dict(map(lambda word: (word, len(word)), words))


def remove_falsy_values(values: list[T]) -> list[T]:
    """
    Remove falsy values from a list.

    Args:
        values: A list of values.

    Returns:
        A list containing only truthy values.
    """
    return list(filter(None, values))


def calculate_running_totals(numbers: list[int]) -> list[int]:
    """
    Calculate cumulative sums of numbers.

    Args:
        numbers: A list of integers.

    Returns:
        A list containing cumulative sums.
    """
    return list(accumulate(numbers))

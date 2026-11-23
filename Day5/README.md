# Day 5 – Functional Programming Utilities

## Overview

This project contains reusable Python utility functions extracted and improved from the Day 3 functional programming exercises.

The module demonstrates functional programming techniques using Python's built-in functions and itertools.

## Functions Included

1. `square_odd_numbers()` – Squares odd numbers.
2. `normalize_names()` – Removes whitespace and converts names to uppercase.
3. `multiply_pairs()` – Multiplies corresponding elements from two lists.
4. `filter_long_words()` – Filters words longer than three characters.
5. `calculate_product()` – Calculates the product of numbers using reduce.
6. `calculate_total_price()` – Calculates the total price of items.
7. `flatten_lists()` – Flattens nested lists using itertools.chain.
8. `create_word_length_dict()` – Creates a dictionary of words and their lengths.
9. `remove_falsy_values()` – Removes falsy values using filter.
10. `calculate_running_totals()` – Calculates cumulative sums using itertools.accumulate.

## Project Structure

```text
Day5/
├── functional_utils.py
├── test_functional_utils.py
├── mathutils.py
├── test_mathutils.py
└── .pre-commit-config.yaml
```

## Requirements

- Python 3.11+
- pytest
- black
- ruff
- mypy
- pre-commit

## Setup

Activate your virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

From the project root:

```bash
pytest -v Day5/test_functional_utils.py
```

## Code Quality Checks

```bash
black Day5/functional_utils.py Day5/test_functional_utils.py

ruff check --ignore C417 Day5/functional_utils.py Day5/test_functional_utils.py

mypy Day5/functional_utils.py
```

## Pre-commit Hooks

Install the hooks:

```bash
pre-commit install
```

Run all hooks:

```bash
pre-commit run --all-files
```

## Learning Outcome

This project demonstrates how to transform practice code into reusable, documented, type-annotated Python modules with automated tests and code-quality checks.
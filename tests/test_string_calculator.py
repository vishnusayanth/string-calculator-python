
import pytest
from string_calculator.calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_sum():
    assert add("1,5") == 6

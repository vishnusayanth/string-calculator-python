
import pytest
from string_calculator.calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_sum():
    assert add("1,5") == 6

def test_many_numbers_sum():
    assert add("1,2,3,4,5") == 15

def test_newlines_and_commas_mix():
    assert add("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    assert add("//;\n1;2") == 3

def test_negative_number_raises_with_value():
    with pytest.raises(ValueError) as excinfo:
        add("-1")
    assert str(excinfo.value) == "negative numbers not allowed -1"

def test_multiple_negatives_all_listed():
    with pytest.raises(ValueError) as excinfo:
        add("1,-2,3,-4")
    assert str(excinfo.value) == "negative numbers not allowed -2,-4"

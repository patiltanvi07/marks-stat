import pytest
from marks_stat import highest, lowest, average, validate_marks

def test_highest():
    assert highest([10, 20, 30, 40]) == 40


def test_lowest():
    assert lowest([10, 20, 30, 40]) == 10


def test_average():
    assert average([10, 20, 30]) == 20


def test_highest_single_mark():
    assert highest([50]) == 50


def test_lowest_single_mark():
    assert lowest([50]) == 50


def test_average_decimal():
    assert average([10, 20, 25]) == 55 / 3


def test_valid_marks():
    validate_marks([0, 50, 75, 100])


def test_invalid_marks():
    with pytest.raises(ValueError):
        validate_marks([85, 72, 105, 64, 78])
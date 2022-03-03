import unittest
from unittest import mock
import pytest
from calculate_grades import calculate_stat


def test_calculate_stat():
    assert calculate_stat([2, 4, 4, 2]) == (3.0, 1.23)
    assert calculate_stat([0]) == (0.0, 0.0)

    with pytest.raises(ZeroDivisionError):
        assert calculate_stat([]) == (3.0, 1.23)

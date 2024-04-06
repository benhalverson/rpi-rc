import pytest
from unittest.mock import patch, MagicMock
from monitor import calculate_frequency, cbf  # Ensure to import your script correctly

def test_calculate_frequency_positive_diff():
    # Test with a positive difference
    diff = 500_000  # microseconds
    frequency = calculate_frequency(diff)
    assert frequency == 2.00  # Expected frequency

def test_calculate_frequency_zero_diff():
    # Test with a difference of zero
    diff = 0  # microseconds
    frequency = calculate_frequency(diff)
    assert frequency is None  # Expected to return None

from exo10 import find_largest_number
from unittest.mock import patch
import io

def test_find_largest_number(capsys):
    # Use patch to simulate user input for testing
    with patch("builtins.input", side_effect=["12", "8", "15"]):
        result = find_largest_number(12, 8, 15)

    # Check if the function returns the correct result
    assert result == 15

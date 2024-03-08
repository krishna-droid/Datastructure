from exo12 import count_palindromes
from unittest.mock import patch
import io

def test_count_palindromes(capsys):
    # Use patch to simulate user input for testing
    with patch("builtins.input", side_effect=[["radar", "level", "python", "madam"]]):
        result = count_palindromes(["radar", "level", "python", "madam"])

    # Check if the function returns the correct result
    assert result == 3

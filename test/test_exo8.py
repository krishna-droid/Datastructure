from exo8 import guess_number
from unittest.mock import patch
import io

def test_guess_number(capsys):
    # Use patch to simulate user input for testing
    with patch("builtins.input", side_effect=["50", "75", "63", "70", "68"]):
        result = guess_number()

    # Capture the printed output to check against
    captured = capsys.readouterr()

    # Check if the function returns True (user guessed correctly)
    assert result is True

    # Check if the correct congratulatory message is printed
    assert "Congratulations! You guessed the correct number" in captured.out

from exo8 import guess_number
from unittest.mock import patch

def test_guess_number(capsys):
    # Use patch to simulate user input for testing
    with patch("builtins.input", side_effect=["50", "75", "63", "70", "68"]):
        result = guess_number()

    # Capture the printed output to check against
    captured = capsys.readouterr()

    # Check if the function returns False (user ran out of attempts)
    assert result is False

    # Check if the correct message for running out of attempts is printed
    assert "Sorry, you've run out of attempts" in captured.out

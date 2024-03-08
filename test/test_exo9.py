from exo9 import draw_pyramid
from unittest.mock import patch
import io

def test_draw_pyramid(capsys):
    # Use patch to simulate user input for testing
    with patch("builtins.input", side_effect=["5"]):
        draw_pyramid(5)

    # Capture the printed output to check against
    captured = capsys.readouterr()

    expected_output = "    *\n   ***\n  *****\n *******\n*********\n"
    
    # Check if the function prints the correct pyramid
    assert captured.out == expected_output

import sys
from io import StringIO
from exo23 import build_binary_tree, print_preorder

def test_print_preorder(capsys):
    tree = build_binary_tree()

    # Redirect stdout to capture the printed output
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    print_preorder(tree)

    # Capture the printed output
    captured = sys.stdout.getvalue()

    # Reset stdout to its original state
    sys.stdout = original_stdout

    expected_output = "1 2 4 5 3 6 7"

    assert captured.strip() == expected_output


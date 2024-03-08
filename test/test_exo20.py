from exo20 import process_bytearray
import pytest

def test_process_bytearray(capsys):
    # Capture the printed output to check against
    initial_byte_array = bytearray([10, 20, 30, 40])

    process_bytearray(initial_byte_array)

    captured = capsys.readouterr()
    assert captured.out == "10\n20\n30\n40\n"

    assert initial_byte_array == bytearray([11, 21, 31, 41])

if __name__ == "__main__":
    pytest.main()

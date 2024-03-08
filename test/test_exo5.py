from exo5 import rotate_right

def test_rotate_right():
    # Test case with positive rotation count
    input_list_1 = [1, 2, 3, 4, 5]
    result_1 = rotate_right(input_list_1, 2)
    assert result_1 == [4, 5, 1, 2, 3]

    # Test case with negative rotation count
    input_list_2 = [10, 20, 30, 40, 50]
    result_2 = rotate_right(input_list_2, -2)
    assert result_2 == [30, 40, 50, 10, 20]

    # Test case with rotation count exceeding the length of the list
    input_list_3 = ['a', 'b', 'c', 'd', 'e']
    result_3 = rotate_right(input_list_3, 8)
    assert result_3 == ['c', 'd', 'e', 'a', 'b']  # Corrected expected result

    # Test case with an empty list
    input_list_4 = []
    result_4 = rotate_right(input_list_4, 3)
    assert result_4 == []

    # Test case with rotation count equal to the length of the list
    input_list_5 = ['x', 'y', 'z']
    result_5 = rotate_right(input_list_5, 3)
    assert result_5 == ['x', 'y', 'z']

from exo4 import unique_elements

def test_unique_elements():
    # Test case with duplicate elements
    input_list_1 = [1, 2, 2, 3, 4, 4, 5]
    result_1 = unique_elements(input_list_1)
    assert result_1 == [1, 2, 3, 4, 5]

    # Test case with no duplicate elements
    input_list_2 = [5, 3, 7, 1, 9]
    result_2 = unique_elements(input_list_2)
    assert sorted(result_2, key=lambda x: (type(x).__name__, x)) == sorted([5, 3, 7, 1, 9], key=lambda x: (type(x).__name__, x))

    # Test case with an empty list
    input_list_3 = []
    result_3 = unique_elements(input_list_3)
    assert result_3 == []

    # Test case with a mix of types
    input_list_4 = [1, "apple", 2, "orange", 3, "apple"]
    result_4 = unique_elements(input_list_4)
    expected_result_4 = [1, "apple", 2, "orange", 3]
    assert sorted(result_4, key=lambda x: (type(x).__name__, x)) == sorted(expected_result_4, key=lambda x: (type(x).__name__, x))

    # Test case with negative numbers
    input_list_5 = [-2, -1, 0, 1, -2, 2]
    result_5 = unique_elements(input_list_5)
    expected_result_5 = [-2, -1, 0, 1, 2]
    assert sorted(result_5, key=lambda x: (type(x).__name__, x)) == sorted(expected_result_5, key=lambda x: (type(x).__name__, x))

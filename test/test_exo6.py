from exo6 import find_largest_tuple

def test_find_largest_tuple():
    # Test case with multiple tuples
    input_tuples_1 = [(1, 2), ('a', 'b', 'c'), (True, False, True, True)]
    result_1 = find_largest_tuple(input_tuples_1)
    assert result_1 == (True, False, True, True)

    # Test case with an empty list
    input_tuples_2 = []
    result_2 = find_largest_tuple(input_tuples_2)
    assert result_2 is None

    # Test case with a single tuple
    input_tuples_3 = [('apple', 'orange', 'banana')]
    result_3 = find_largest_tuple(input_tuples_3)
    assert result_3 == ('apple', 'orange', 'banana')

    # Test case with tuples of equal length
    input_tuples_4 = [(1, 2, 3), ('x', 'y', 'z'), ('a', 'b', 'c')]
    result_4 = find_largest_tuple(input_tuples_4)
    assert result_4 == (1, 2, 3)

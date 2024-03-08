from exo7 import reverse_tuples

def test_reverse_tuples():
    # Test case with multiple tuples
    input_tuples_1 = [(1, 2), ('a', 'b', 'c'), (True, False, True, True)]
    result_1 = reverse_tuples(input_tuples_1)
    assert result_1 == [(2, 1), ('c', 'b', 'a'), (True, True, False, True)]

    # Test case with an empty list
    input_tuples_2 = []
    result_2 = reverse_tuples(input_tuples_2)
    assert result_2 == []

    # Test case with a single tuple
    input_tuples_3 = [('apple', 'orange', 'banana')]
    result_3 = reverse_tuples(input_tuples_3)
    assert result_3 == [('banana', 'orange', 'apple')]

    # Test case with tuples of equal length
    input_tuples_4 = [(1, 2, 3), ('x', 'y', 'z'), ('a', 'b', 'c')]
    result_4 = reverse_tuples(input_tuples_4)
    assert result_4 == [(3, 2, 1), ('z', 'y', 'x'), ('c', 'b', 'a')]

from exo17 import symmetric_difference_of_sets

def test_symmetric_difference_of_sets():
    # Test case with common elements
    result_1 = symmetric_difference_of_sets({1, 2, 3, 4}, {3, 4, 5, 6})
    assert result_1 == {1, 2, 5, 6}

    # Test case with no common elements
    result_2 = symmetric_difference_of_sets({10, 20, 30}, {40, 50, 60})
    assert result_2 == {10, 20, 30, 40, 50, 60}

    # Test case with one empty set
    result_3 = symmetric_difference_of_sets({1, 2, 3}, set())
    assert result_3 == {1, 2, 3}

    # Test case with both empty sets
    result_4 = symmetric_difference_of_sets(set(), set())
    assert result_4 == set()

    # Test case with repeated elements
    result_5 = symmetric_difference_of_sets({1, 2, 3, 3, 4, 4}, {3, 4, 5, 5, 6, 6})
    assert result_5 == {1, 2, 5, 6}

    # Test case with mixed types
    result_6 = symmetric_difference_of_sets({1, 2, 'apple'}, {2, 'orange', 'apple'})
    assert result_6 == {1, 'orange'}

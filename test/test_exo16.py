from exo16 import intersection_of_sets

def test_intersection_of_sets():
    # Test case with common elements
    result_1 = intersection_of_sets({1, 2, 3, 4}, {3, 4, 5, 6})
    assert result_1 == {3, 4}

    # Test case with no common elements
    result_2 = intersection_of_sets({10, 20, 30}, {40, 50, 60})
    assert result_2 == set()

    # Test case with one empty set
    result_3 = intersection_of_sets({1, 2, 3}, set())
    assert result_3 == set()

    # Test case with both empty sets
    result_4 = intersection_of_sets(set(), set())
    assert result_4 == set()

    # Test case with repeated elements
    result_5 = intersection_of_sets({1, 2, 3, 3, 4, 4}, {3, 4, 5, 5, 6, 6})
    assert result_5 == {3, 4}

    # Test case with mixed types
    result_6 = intersection_of_sets({1, 2, 'apple'}, {2, 'orange', 'apple'})
    assert result_6 == {2, 'apple'}

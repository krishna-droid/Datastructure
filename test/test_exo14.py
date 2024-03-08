from exo14 import filter_students

def test_filter_students():
    # Test case with mixed scores
    scores_dict_1 = {"Alice": 18, "Bob": 12, "Charlie": 15, "David": 20}
    result_1 = filter_students(scores_dict_1)
    assert result_1 == {"Alice": 18, "Charlie": 15, "David": 20}

    # Test case with all scores below 15
    scores_dict_2 = {"Eva": 14, "Frank": 13, "Grace": 11}
    result_2 = filter_students(scores_dict_2)
    assert result_2 == {}

    # Test case with an empty dictionary
    scores_dict_3 = {}
    result_3 = filter_students(scores_dict_3)
    assert result_3 == {}

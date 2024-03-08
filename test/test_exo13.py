from exo13 import count_palindromes

def test_count_palindromes():
    # Test case with palindromes and non-palindromes
    words_list_1 = ["radar", "level", "python", "madam"]
    result_1 = count_palindromes(words_list_1)
    assert result_1 == 3

    # Test case with an empty list
    words_list_2 = []
    result_2 = count_palindromes(words_list_2)
    assert result_2 == 0

    # Test case with all palindromes
    words_list_3 = ["noon", "deed", "refer"]
    result_3 = count_palindromes(words_list_3)
    assert result_3 == 3

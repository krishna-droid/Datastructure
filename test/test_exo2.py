from exo2 import extract_word_simple, extract_word_negative_indices, extract_phrase_slicing, reverse_string

def test_extract_word_simple():
    assert extract_word_simple("Python est un langage de programmation puissant et facile à apprendre.") == "Python"

def test_extract_word_negative_indices():
    assert extract_word_negative_indices("Python est un langage de programmation puissant et facile à apprendre.") == "apprendre."

def test_extract_phrase_slicing():
    assert extract_phrase_slicing("Python est un langage de programmation puissant et facile à apprendre.") == ["langage", "de", "programmation"]

def test_reverse_string():
    expected_reversed_string = ".erdnerppa à elicaf te tnassiup noitammargorp ed egagnal nu tse nohtyP"
    assert reverse_string("Python est un langage de programmation puissant et facile à apprendre.") == expected_reversed_string


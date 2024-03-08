def extract_word_simple(input_string):
    return input_string.split()[0]

def extract_word_negative_indices(input_string):
    words = input_string.split()
    return words[-1]

def extract_phrase_slicing(input_string):
    return input_string.split(" ")[3:6]

def reverse_string(input_string):
    return input_string[::-1]

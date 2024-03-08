def count_palindromes(words_list):
    # Function to check if a word is a palindrome
    def is_palindrome(word):
        return word == word[::-1]

    # Count the number of palindromes in the list
    palindrome_count = sum(1 for word in words_list if is_palindrome(word))

    return palindrome_count

# Uncomment the line below to test the function
# count_palindromes(["radar", "level", "python", "madam"])

def count_upper_lower(input_string):
    
    uppercase_count = 0
    lowercase_count = 0

    
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    
    return {"uppercase_count": uppercase_count, "lowercase_count": lowercase_count}
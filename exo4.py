def unique_elements(input_list):
    # Use a set to keep track of unique elements
    unique_set = set()
    
    # Iterate through the input list and add elements to the set
    for element in input_list:
        unique_set.add(element)
    
    # Convert the set back to a list and return
    return list(unique_set)

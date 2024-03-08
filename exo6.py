def find_largest_tuple(tuple_list):
    if not tuple_list:
        return None  # Return None for an empty list

    largest_tuple = max(tuple_list, key=len)
    return largest_tuple

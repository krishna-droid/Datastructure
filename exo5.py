def rotate_right(input_list, rotation_count):
    if not input_list:
        return input_list  # Return the input list as-is for an empty list

    # Determine the effective rotation count
    effective_rotation = rotation_count % len(input_list)

    # Perform the rotation
    rotated_list = input_list[-effective_rotation:] + input_list[:-effective_rotation]

    return rotated_list

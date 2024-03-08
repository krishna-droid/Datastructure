def filter_students(scores_dict):
    # Filter students with average scores greater than or equal to 15
    high_scorers = {name: score for name, score in scores_dict.items() if score >= 15}

    return high_scorers

# Uncomment the line below to test the function
# filter_students({"Alice": 18, "Bob": 12, "Charlie": 15, "David": 20})

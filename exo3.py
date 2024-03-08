def add_two_numbers(num1_str, num2_str):
    # Convert input strings to integers
    num1 = int(num1_str)
    num2 = int(num2_str)

    # Calculate the sum
    result_sum = num1 + num2

    # Return the result in different forms
    return {
        'num1': num1,
        'num2': num2,
        'sum': result_sum,
        'sum_str': f"The sum of {num1} and {num2} is {result_sum}.",
        'sum_formatted': f"{num1} + {num2} = {result_sum}"
    }

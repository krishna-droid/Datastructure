from exo3 import add_two_numbers

def test_add_two_numbers():
    result = add_two_numbers("5", "7")

    assert result['num1'] == 5
    assert result['num2'] == 7
    assert result['sum'] == 12
    assert result['sum_str'] == "The sum of 5 and 7 is 12."
    assert result['sum_formatted'] == "5 + 7 = 12"

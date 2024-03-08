def decode_message(encoded_message):
    # Split the encoded message into a list of ASCII values
    ascii_values = encoded_message.split()

    # Convert ASCII values to characters and join them to form the decoded message
    decoded_message = ''.join(chr(int(value)) for value in ascii_values)

    return decoded_message

# Uncomment the line below to test the function
# decode_message("72 101 108 108 111")

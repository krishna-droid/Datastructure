def process_bytearray(byte_array):
    for i in range(len(byte_array)):
        print(byte_array[i])
        byte_array[i] += 1

if __name__ == "__main__":
    initial_byte_array = bytearray([10, 20, 30, 40])
    print("Initial bytearray:", initial_byte_array)

    process_bytearray(initial_byte_array)

    print("Updated bytearray:", initial_byte_array)

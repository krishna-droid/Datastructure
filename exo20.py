def process_bytearray(byte_array):
    for i in range(len(byte_array)):
        print(byte_array[i])
        byte_array[i] += 1

if __name__ == "__main__":
    byte_array = bytearray([10, 20, 30, 40])
    process_bytearray(byte_array)
    print("Updated bytearray:", byte_array)

def validUTF8(data):
    num_bytes = 0  # Number of bytes in the current UTF-8 character

    for byte in data:
        # We only need the 8 least significant bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character must start with 0xxxxxxx
                return False
        else:
            # Check that the byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If we finish and num_bytes is 0, it means we had complete characters
    return num_bytes == 0

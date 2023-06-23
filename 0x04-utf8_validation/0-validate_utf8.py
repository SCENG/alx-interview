#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If the byte starts with 0, it is a single-byte character
        if num_bytes == 0:
            # Check if the most significant bit is 0
            if byte >> 7 == 0b0:
                continue
            # Check the number of bytes in the current character
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte starts with 10, indicating it is a continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # All characters should have been validated and completed
    return num_bytes == 0

#!/usr/bin/python3
''' validate UTF-8 encoding '''

def validUTF8(data):
    '''
    Determines if a given data set represents a valid UTF-8 encoding

    Return: True if data is a valid UTF-8 encoding, else return False
    '''

    # Check the first byte whether it begins with 10
    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:

        mask_n_byte = 1 << 7

        if number_bytes == 0:
            # Count number of bytes
            while mask_n_byte & i:
                number_bytes += 1
                mask_n_byte = mask_n_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Return false if not valid
            if not (i & mask1 and not (i & mask2)):
                return False

        number_bytes -= 1

    # Return true if valid
    if number_bytes == 0:
        return True

    return False

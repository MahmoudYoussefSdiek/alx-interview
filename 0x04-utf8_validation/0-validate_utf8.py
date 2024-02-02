#!/usr/bin/python3
"""
This module contains the validUTF8 function
"""


def validUTF8(data):
    """
    Check if a list of integers follows the UTF-8 encoding
    """
    count = 0
    for num in data:
        if count == 0:
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1
    return True

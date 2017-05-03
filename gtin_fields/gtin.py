""" Code for GTIN-14 checksum validation.

TODO: This code should be pushed into python-stdnum.  Within python stdnum
should move ean.py to gtin.py.

The code in this file is nearly identical to the stdnum/ean.py code.
"""
from stdnum.ean import calc_check_digit, compact
from stdnum.exceptions import (InvalidChecksum, InvalidFormat, InvalidLength,
                               ValidationError)


def validate(number):
    """Checks to see if the number provided is a valid GTIN code.  Will
    validate GTIN-14, GTIN-13 (EAN-13), GTIN-12 (UPC-A), and GTIN-8 (EAN-8)
    codes. This checks the length and the check bit but does not check whether
    a known GS1 Prefix and company identifier are referenced."""
    number = compact(number)
    if not number.isdigit():
        raise InvalidFormat()
    if len(number) not in (14, 13, 12, 8):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number


def is_valid(number):
    """Checks to see if the number provided is a valid GTIN code (see
    validate). This checks the length and the check bit but does not check
    whether a known GS1 Prefix and company identifier are referenced."""
    try:
        return bool(validate(number))
    except ValidationError:
        return False

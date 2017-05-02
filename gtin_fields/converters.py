""" Converters related to GTIN fields. """
from stdnum import ean


def upce_to_upca(upce, validate=True):
    """ Converts an UPC-E code to a 12 digit UPC-A code.

    If code is 7 digits and first digit is not zero then will form 8 digit
    code by pading left with a zero (assumes the left zero was lost somewhere
    in conversion to int).

    See:
    https://stackoverflow.com/questions/31539005/how-to-convert-a-upc-e-barcode-to-a-upc-a-barcode
    http://www.taltech.com/barcodesoftware/symbologies/upc

    Args:
      upce (str or int): The upce code.  Will properly handle a 6 or 8 digit
          code or an 8 digit code that lost its leading zero.
      validate: Will validate the length of input, the 'S' leader digit if an 8
          digit code, and the checksum (if given an 8 digit code).

    Returns:
      (str): The UPC-A code.
    """
    given_upce = str(upce)

    # can safely zero pad left a seven digit upce (is missing its left zero)
    if (len(given_upce) == 7) and (given_upce[0] != '0'):
        pad = '0'
    else:
        pad = ''

    padded_upce = pad + given_upce

    if validate:
        if len(padded_upce) not in (6, 8):
            raise ValueError(
                "Provided UPC-E {} must be 6 or 8 digits!".format(
                    repr(given_upce)
                )
            )

        if (len(padded_upce) == 8 and padded_upce[0] not in ('0', '1')):
            raise ValueError("8 digit UPC-E must begin with 0 or 1")

    given_6_digit_upce = (len(padded_upce) == 6)
    upce6 = padded_upce if given_6_digit_upce else padded_upce[1:7]

    # upce6 digit names: abcdeN
    map_id = int(upce6[-1])  # N
    ab_prefix = upce6[0:2]  # ab

    if map_id >= 5:
        core = upce6[2:5], '0' * 4, map_id   # cde0000N
    elif map_id <= 2:
        core = map_id, '0' * 4, upce6[2:5]  # N0000cde
    elif map_id == 3:
        core = upce6[2], '0' * 5, upce6[3:5]   # c00000de
    elif map_id == 4:
        core = upce6[2:4], '0' * 5, upce6[4]  # cd00000e

    # ab + core
    no_leader_no_checksum = ab_prefix + ''.join(map(str, core))

    # add leader, also called 'S' digit
    leader = '0' if given_6_digit_upce else padded_upce[0]
    with_leader_no_checksum = leader + no_leader_no_checksum

    if given_6_digit_upce:
        with_checksum = with_leader_no_checksum\
            + ean.calc_check_digit(with_leader_no_checksum)
    else:
        with_checksum = with_leader_no_checksum + given_upce[-1]
        if validate:
            ean.validate(with_checksum)

    return with_checksum


def to_gtin14(value):
    """ Convert various product codes to  to GTIN-14.

    Will convert UPC-A (GTIN-12), GTIN-13 (EAN / UCC-13), GTIN-8 (EAN / UCC-8)
    to GTIN-14 by left zero padding.

    See http://www.gtin.info/

    Returns:
      (str): The GTIN-14 code.
    """
    return str(value).zfill(14)


upca_to_gtin14 = to_gtin14
ean_to_gtin14 = to_gtin14
gtin8_to_gtin14 = to_gtin14


def to_ean(value):
    """ Convert UPC-A (GTIN-12) to EAN-13.

    See:
        http://www.gtin.info/
        https://www.nationwidebarcode.com/are-upc-a-and-ean-13-the-same/

    Returns:
      (str): An EAN-13 code.
    """
    return str(value).zfill(13)


upca_to_ean = to_ean
upca_to_ean13 = to_ean
upca_to_gtin13 = to_ean

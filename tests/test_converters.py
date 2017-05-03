from django.test import SimpleTestCase
from gtin_fields import converters
from stdnum.exceptions import InvalidChecksum


class ConvertersTest(SimpleTestCase):
    """ Test the converters. """

    def test_upce_to_upca(self):
        """ Converts UPC-E to UPC-A. """
        upce_to_upca = {

            # map_id == 1
            '425261': '042100005264',
            '425211': '042100005219',
            '425231': '042100005233',
            '425241': '042100005240',

            # map_id == 2
            '425262': '042200005263',

            # map_id == 3
            '425263': '042500000265',

            # map_id == 4
            '425264': '042520000061',

            # map_id >= 5
            '425265': '042526000058',
            '425266': '042526000065',
            '425267': '042526000072',
            '425268': '042526000089',
            '425269': '042526000096',

            # with leader and checksum
            '04252614': '042100005264',
            '04252119': '042100005219',
            '04252313': '042100005233',
            '04252410': '042100005240',

            # seven digits (missing left zero)
            '4252614': '042100005264',
            '4252119': '042100005219',
            '4252313': '042100005233',
            '4252410': '042100005240',
        }
        for upce, upca in upce_to_upca.items():
            self.assertEqual(converters.upce_to_upca(upce), upca)

    def test_upce_to_upca_bad_length(self):
        """ Raise a ValueError. """
        bad_lengths = [
            '42526',  # too short
            '0252410',  # seven digits but not a missing left zero
            '042526149',  # 9 digits
        ]
        for bad_length_upce in bad_lengths:
            with self.assertRaises(ValueError):
                converters.upce_to_upca(bad_length_upce)

    def test_upce_to_upca_bad_checksum(self):
        """ Raises a stdnum.exceptions.InvalidChecksum error. """
        bad_checksum_upce = '04252616'
        with self.assertRaises(InvalidChecksum):
            converters.upce_to_upca(bad_checksum_upce)

        # will pass silently if validation turned off:
        self.assertEqual(
            converters.upce_to_upca(bad_checksum_upce, validate=False),
            '042100005266'
        )

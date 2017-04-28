from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from gtin_fields import converters
from gtin_fields.validators import ISBNValidator

# class ConvertersTest(SimpleTestCase):
    # """ Test the converters. """

    # def test_upce_to_upca(self):
        # upce_to_upca = {
            # '425261': '042100005264',
            # '425211': '042100005219',
            # '425231': '042100005233',
            # '425241': '042100005240',
        # }
        # for upce, upca in upce_to_upca.items():
            # self.assertEqual(converters.upce_to_upca(upce), upca)


# class ISBNValidatorTest(SimpleTestCase):

    # def test_calidation(self):
        # # Short
        # with self.assertRaises(ValidationError):
            # ISBNValidator('111')

        # # Long
        # with self.assertRaises(ValidationError):
            # ISBNValidator('12345678901234')

        # # ISBN w Error
        # with self.assertRaises(ValidationError):
            # ISBNValidator('0765348275')

        # # Valid ISBN10
        # ISBNValidator('0765348276')

        # # Valid ISBN13
        # ISBNValidator('9780765348272')

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from gtin_fields import converters
from gtin_fields.validators import ISBNValidator


class ISBNFieldTest(SimpleTestCase):

    def test_validation(self):
        # Short
        with self.assertRaises(ValidationError):
            ISBNValidator('111')

        # Long
        with self.assertRaises(ValidationError):
            ISBNValidator('12345678901234')

        # ISBN w Error
        with self.assertRaises(ValidationError):
            ISBNValidator('0765348275')

        # Valid ISBN10
        ISBNValidator('0765348276')

        # Valid ISBN13
        ISBNValidator('9780765348272')

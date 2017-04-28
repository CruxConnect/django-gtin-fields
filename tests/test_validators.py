from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from gtin_fields.validators import ISBNValidator


class ValidatorTestMixin:
    """ Check validity of various values.

    Expects the following attributes on self:

        self.invalid (list): List of values that will raise ValidationError
        self.valid (list): List of values that *not* raise ValidationError
        self.validator (callable): The callable that takes the value to be validated.
    """
    def test_validation(self):
        for value in self.invalid:
            with self.assertRaises(ValidationError):
                self.validator(value)

        for value in self.valid:
            self.assertIsNone(self.validator(value))


class ISBNValidatorTest(SimpleTestCase, ValidatorTestMixin):

    def setUp(self):
        self.validator = ISBNValidator

        self.invalid = [
            '111',  # short
            '12345678901234',  # long
            '0765348275',  # checksum error
        ]

        self.valid = [
            '0765348276',  # ISBN10
            '9780765348272',  # ISBN13
        ]
        super().setUp()

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from gtin_fields import validators

from .product_codes import CODES


class ValidatorTestMixin:
    """ Check validity of various values.

    Expects the following attributes on self:

        self.codes (dict): Should have keys 'valid' and 'invalid', each
            pointing to a list of product codes.
        self.validator (callable): The callable that takes the value to be
            validated.
    """
    def test_validation(self):
        for value in self.codes['invalid']:
            with self.assertRaises(ValidationError):
                self.validator(value)

        for value in self.codes['valid']:
            self.assertIsNone(self.validator(value))


class ISBNValidatorTest(SimpleTestCase, ValidatorTestMixin):
    codes = CODES['ISBN']
    validator = validators.ISBNValidator


class UPCAValidatorTest(SimpleTestCase, ValidatorTestMixin):
    validator = validators.UPCAValidator
    codes = CODES['UPCA']


class EAN13ValidatorTest(SimpleTestCase, ValidatorTestMixin):
    validator = validators.EAN13Validator
    codes = CODES['EAN13']


class GTIN14ValidatorTest(SimpleTestCase, ValidatorTestMixin):
    validator = validators.GTIN14Validator
    codes = CODES['GTIN14']


class ASINValidatorTest(SimpleTestCase, ValidatorTestMixin):
    """ Accepts any alphanumeric characters in a 10 digit code.

    This is the 'loose' definition of an ASIN (i.e., Amazon could start
    using any codes within the alpha-numeric range).
    """
    validator = validators.ASINValidator
    codes = CODES['ASIN']


class ASINStrictValidatorTest(SimpleTestCase, ValidatorTestMixin):
    """ The ASINStrictValidator must follow conventional ASIN patterns. """
    validator = validators.ASINStrictValidator
    codes = CODES['ASIN_strict']

""" Test fields. """
from itertools import zip_longest

from django.core.exceptions import ValidationError
from django.test import TestCase

from gtin_fields import converters
from gtin_fields.validators import ISBNValidator
from tests.app.models import MockProduct
from tests.product_codes import CODES


class FieldTestMixin:
    """ Test a Field for validationa and correct round-trip saving.

    Expects a couple variables to be defined on self:

        self.codes (dict): A dict with 'valid' and 'invalid' keys, each with an
            iterable of valid and invalid codes.
        self.key (str): The key for assigning the value on MockProduct (e.g.,
            'isbn')
    """
    def test_full_clean(self):
        """ Should not raise an error. """
        for code in self.codes['valid']:
            product = MockProduct(**{self.key: code})
            product.full_clean()

        # assert to indicate that valid codes were in fact tested
        self.assertTrue(self.codes)

    def test_full_clean_on_invalid(self):
        """ Should raise a ValidationError. """
        for code in self.codes['invalid']:
            with self.assertRaises(ValidationError):
                product = MockProduct(**{self.key: code})
                product.full_clean()

    def test_saving(self):
        """ Can save all valid objects to the db. """
        for code in self.codes['valid']:
            product = MockProduct(**{self.key: code})
            product.full_clean()
            product.save()

        for (code, obj) in zip_longest(self.codes['valid'], MockProduct.objects.all()):
            self.assertEqual(getattr(obj, self.key), code)


class ASINFieldTest(FieldTestMixin, TestCase):
    key = 'asin'
    codes = CODES['ASIN']


class ASINStrictFieldTest(FieldTestMixin, TestCase):
    key = 'asin_strict'
    codes = CODES['ASIN_strict']


class UPCAFieldTest(FieldTestMixin, TestCase):
    key = 'upca'
    codes = CODES['UPCA']


class GTIN14FieldTest(FieldTestMixin, TestCase):
    key = 'gtin14'
    codes = CODES['GTIN14']


class ISBNFieldTest(FieldTestMixin, TestCase):
    key = 'isbn'
    codes = CODES['ISBN']


class EAN13FieldTest(FieldTestMixin, TestCase):
    key = 'ean13'
    codes = CODES['EAN13']

""" Test the forms related to the model. """
from django.forms import ModelForm
from django.test import TestCase

from tests.app.models import MockProduct
from tests.product_codes import CODES


class ProductForm(ModelForm):
    class Meta:
        model = MockProduct
        exclude = []


class FormTestMixin:
    """ Test a GTIN ModelForm.

    Expects:

        self.code (dict): 'valid' and 'invalid' keys, each with a list of
            valid and invalid codes.
        self.key (str): The attribute being updated / created.
    """
    def test_form_valid(self):
        for code in self.code['valid']:
            form = ProductForm({self.key: code})
            self.assertEqual(form.errors, {})
            self.assertTrue(form.is_valid())
            self.assertEqual(form.cleaned_data[self.key], code)
            new_product = form.save()
            self.assertEqual(getattr(new_product, self.key), code)

    def test_form_invalid(self):
        for code in self.code['invalid']:
            form = ProductForm({self.key: code})
            self.assertTrue(self.key in form.errors)
            self.assertFalse(form.is_valid())
            for value in form.cleaned_data.values():
                self.assertEqual(value, '')
            with self.assertRaises(ValueError):
                form.save()


class ISBNFormTest(TestCase, FormTestMixin):
    code = CODES['ISBN']
    key = 'isbn'


class UPCAFormTest(TestCase, FormTestMixin):
    code = CODES['UPCA']
    key = 'upca'


class EAN13FormTest(TestCase, FormTestMixin):
    code = CODES['EAN13']
    key = 'ean13'


class GTIN14FormTest(TestCase, FormTestMixin):
    code = CODES['GTIN14']
    key = 'gtin14'


class ASINFormTest(TestCase, FormTestMixin):
    code = CODES['ASIN']
    key = 'asin'


class ASINStrictFormTest(TestCase, FormTestMixin):
    code = CODES['ASIN_strict']
    key = 'asin_strict'

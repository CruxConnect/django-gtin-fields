from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from gtin_fields import validators


class ValidatorTestMixin:
    """ Check validity of various values.

    Expects the following attributes on self:

        self.invalid (list): List of values that will raise ValidationError
        self.valid (list): List of values that *not* raise ValidationError
        self.validator (callable): The callable that takes the value to be
            validated.
    """
    def test_validation(self):
        for value in self.invalid:
            with self.assertRaises(ValidationError):
                self.validator(value)

        for value in self.valid:
            self.assertIsNone(self.validator(value))


class ISBNValidatorTest(SimpleTestCase, ValidatorTestMixin):

    def setUp(self):
        self.validator = validators.ISBNValidator

        self.invalid = [
            '111',  # short
            '12345678901234',  # long
            '0765348275',  # checksum error
            '076534827X',  # bad character
        ]

        self.valid = [
            '0765348276',  # ISBN10
            '9780765348272',  # ISBN13
        ]
        super().setUp()


class UPCAValidatorTest(SimpleTestCase, ValidatorTestMixin):

    def setUp(self):
        self.validator = validators.UPCAValidator

        self.invalid = [
            '04210000526',  # short
            '1042100005219',  # long
            '042100005265',  # checksum error
            '042100X05264',  # bad character
        ]

        self.valid = [
            '042100005264',
            '042100005219',
            '042100005233',
            '042100005240',
            '042200005263',
            '042500000265',
            '042520000061',
            '042526000058',
            '042526000065',
            '042526000072',
            '042526000089',
            '042526000096',
            '042100005264',
            '042100005219',
            '042100005233',
            '042100005240',
        ]

        super().setUp()


class EAN13ValidatorTest(SimpleTestCase, ValidatorTestMixin):

    def setUp(self):
        self.validator = validators.EAN13Validator

        self.invalid = [
            '780471117094',  # short
            '14006381333931',  # long
            '9780471117093',  # checksum error
            '978L471117093',  # bad character
        ]

        self.valid = [
            '9780471117094',
            '4006381333931',
        ]

        super().setUp()


class GTIN14ValidatorTest(SimpleTestCase, ValidatorTestMixin):

    def setUp(self):
        self.validator = validators.GTIN14Validator

        self.invalid = [
            '0123456000018',  # short
            '010123456000015',  # long
            '00123456000016',  # checksum error
            '001234560Y0018',  # bad character
        ]

        self.valid = [
            '00123456000018',
            '10123456000015',
            '70123456000017',
            '71123456000016',
        ]

        super().setUp()


class ASINValidatorTest(SimpleTestCase, ValidatorTestMixin):

    def setUp(self):
        """ Accepts any alphanumeric characters in a 10 digit code.

        This is the 'loose' definition of an ASIN (i.e., Amazon could start
        using any codes within the alpha-numeric range).
        """
        self.validator = validators.ASINValidator

        self.invalid = [
            'B06Y125DW',  # short
            'B06Y125DWZZ',  # long
            'B06Y125-WZ',  # bad character
            'B06Y125_WZ',  # bad character
        ]

        self.valid = [
            'B06Y125DWZ',
            'B01G29XQ30',
            'B000N2HBSO',
            '054792822X',
            '0000000000',
            'ZZZZZZZZZZ',
        ]

        super().setUp()


class ASINStrictValidatorTest(SimpleTestCase, ValidatorTestMixin):
    """ Test ASIN Validator . """

    def setUp(self):
        """ The ASINStrictValidator must follow conventional ASIN patterns. """
        self.validator = validators.ASINStrictValidator

        self.invalid = [
            'B06Y125DW',  # short
            'B06Y125DWZZ',  # long
            'B06Y125-WZ',  # bad character
            'B06Y125_WZ',  # bad character
            'ZZZZZZZZZZ',  # doesn't start with 'B'
        ]

        self.valid = [
            'B06Y125DWZ',
            'B01G29XQ30',
            'B000N2HBSO',
            '054792822X',
            '0000000000',
            'B000000000',
            '000000000X',
        ]

        super().setUp()

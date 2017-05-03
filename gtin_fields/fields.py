from django.db.models import CharField
from gtin_fields import validators


class ProductCodeFieldBase(CharField):
    """ Base class for all these product code fields.

    Expects the variable _primary_validator (one of the
    gtin_fields.validators) on self.  The _validator_class object should
    have 'valid_lengths' and 'verbose_object_name'.
    """
    def __init__(self, *args, **kwargs):
        new_kwargs = dict(
            dict(
                max_length=max(self._primary_validator.valid_lengths),
                verbose_name=self._primary_validator.verbose_object_name,
                validators=kwargs.get(
                    'validators', []
                ) + [self._primary_validator.validate],
            ),
            **kwargs
        )
        super().__init__(*args, **new_kwargs)

    def formfield(self, **kwargs):
        new_kwargs = dict(
            dict(
                max_length=max(self._primary_validator.valid_lengths),
                min_length=min(self._primary_validator.valid_lengths),
                validators=[self._primary_validator.validate],
            ),
            **kwargs
        )
        return super().formfield(**new_kwargs)

    def __str__(self):
        return self.value


class ISBNField(ProductCodeFieldBase):
    _primary_validator = validators.ISBNValidator


class UPCAField(ProductCodeFieldBase):
    _primary_validator = validators.UPCAValidator


class EAN13Field(ProductCodeFieldBase):
    _primary_validator = validators.EAN13Validator


class GTIN14Field(ProductCodeFieldBase):
    _primary_validator = validators.GTIN14Validator


class ASINField(ProductCodeFieldBase):
    """ Amazon Standard Identification Number field.

    If initialized with strict=True then will use the ASINStrictValidator,
    otherwise ASINValidator.
    """
    _primary_validator = validators.ASINValidator

    def __init__(self, *args, **kwargs):
        if kwargs.pop('strict', None):
            self._primary_validator = validators.ASINStrictValidator
        super().__init__(*args, **kwargs)

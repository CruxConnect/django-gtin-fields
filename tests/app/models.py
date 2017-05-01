""" Models for testing. """
from django.db import models

from gtin_fields.fields import ASINField, EAN13Field, GTIN14Field, ISBNField, UPCAField


NOT_REQUIRED = dict(null=True, blank=True)


class MockProduct(models.Model):
    asin = ASINField(**NOT_REQUIRED)
    asin_strict = ASINField(strict=True, **NOT_REQUIRED)
    upca = UPCAField(**NOT_REQUIRED)
    gtin14 = GTIN14Field(**NOT_REQUIRED)
    isbn = ISBNField(**NOT_REQUIRED)
    ean13 = EAN13Field(**NOT_REQUIRED)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

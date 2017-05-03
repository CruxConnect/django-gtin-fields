""" Models for testing. """
from django.db import models
from gtin_fields import fields

NOT_REQUIRED = dict(null=True, blank=True)


class MockProduct(models.Model):
    asin = fields.ASINField(**NOT_REQUIRED)
    asin_strict = fields.ASINField(strict=True, **NOT_REQUIRED)
    upca = fields.UPCAField(**NOT_REQUIRED)
    gtin14 = fields.GTIN14Field(**NOT_REQUIRED)
    isbn = fields.ISBNField(**NOT_REQUIRED)
    ean13 = fields.EAN13Field(**NOT_REQUIRED)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

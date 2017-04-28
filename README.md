# django-gtin-fields

Provides django model fields to store and validate commonly used GTIN related product identifiers.

## Requirements

It has been tested on

* Python >= 3.5
* Django 1.10

## Installation

Using Pypi

```bash
$ pip install django-gtin-fields
```

## Usage 

Add `gtin_fields` to `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = (
	...
	'gtin_fields',
)
```

Use whichever fields you want in your model.

```python
from django.db import models
from gtin_fields import ISBNField

class Book(models.Model):
	...
	isbn = ISBNField()  # ISBN10 or ISBN13
    upc = UPCAField()  # UPC-A field (12 digit standard UPC)
    ean = EAN13Field()  # EAN-13
    gtin = GTIN14Field()  # GTIN-14

    # not technically GTIN, but commonly used:
    asin = ASINField()  # Amazon Standard Identification Number
```

Converters can help you coerce input between some kinds of input.  For
example:

```python
from gtin_fields import converters

# 6 digit UPC-E
converters.upce_to_upca('425261')  # => '042100005264' (UPC-A)

# 8 digit UPC-E
converters.upce_to_upca('04252614')  # => '042100005264' (UPC-A)

# UPC-A to GTIN-14
converters.upca_to_gtin14('142100005264')  # => "00142100005264' (GTIN-14)

# EAN-13 to GTIN-14
converters.ean_to_gtin14('3142100005264')  # => "01142100005264' (GTIN-14)

# EAN-8 (GTIN-8) to GTIN-14
converters.gtin8_to_gtin14('66425261')  # => '00000066425261' (GTIN-14)

# UPC-A (GTIN-12) to EAN-13 / GTIN-13
converters.upca_to_ean13('142100005264')  # => '0142100005264' (EAN-13)
```

It will raise ValidationError when the number provided is invalid

## TODO

* Implement coverage report through tox
* Finish coverage of converter functions
* Get rest of validators tested
* Get all fields working
* Test all fields
* Upload to pypi

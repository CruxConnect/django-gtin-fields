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

Add gtin_fields to INSTALLED_APPS

```python
# settings.py
INSTALLED_APPS = (
	...
	'gtin_fields',
)
```

Use a field in your model.

```python
from django.db import models
from gtin_fields import ISBNField

class Book(models.Model):
	isbn = ISBNField()
	...
```

It will raise ValidationError when the number provided is invalid

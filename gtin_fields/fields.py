from .validators import ISBNValidator
from django.db.models import CharField


class ISBNField(CharField):

    def __init__(self, *args, **kwargs):

        # Max length is 13 chars for ISBN12
        kwargs['max_length'] = 13
        kwargs['verbose_name'] = u'ISBN'
        kwargs['validators'] = [ISBNValidator]
        super(ISBNField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'max_length': 13,
            'min_length': 10,
            'validators': [ISBNValidator],
        }
        defaults.update(kwargs)
        return super(ISBNField, self).formfield(**defaults)

    def __unicode__(self):
        return self.value


class UPCField(CharField):

    def __init__(self, *args, **kwargs):

        # Max length is 13 chars for ISBN12
        kwargs['max_length'] = 12
        kwargs['verbose_name'] = u'UPC-A'
        kwargs['validators'] = [UPCValidator]
        super(UPCField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'max_length': 12,
            'min_length': 6,
            'validators': [UPCValidator],
        }
        defaults.update(kwargs)
        return super(UPCField, self).formfield(**defaults)

    def __unicode__(self):
        return self.value

import sys
from os import path

from django.db import models
from django.utils.dateparse import date_re
from django.core.exceptions import ValidationError

from necal import forms
# sys.path.append(path.join(path.dirname(__file__), '../necal_py'))
sys.path.append('..')

from necal_py import bs


def parse_date(value):
    """Parse a string and return a nepali_datetime_field.date.

    Raise ValueError if the input is well formatted but not a valid date.
    Return None if the input isn't well formatted.
    """
    match = date_re.match(value)
    if match:
        kw = {k: int(v) for k, v in match.groupdict().items()}
        return bs.date(**kw)


class NepaliCalendar(models.DateField):
    # Add source/link for field customization
    description = "Nepali Calendar Field"

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': forms.NepaliDateField,
            **kwargs,
        })

    def from_db_value(self, value, expression, connection):
        return bs.date.from_datetime_date(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return self.to_python(value).to_datetime_date()

    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, bs.date):
            return value
        try:
            parsed = parse_date(value)
            if parsed is not None:
                return parsed

        except ValueError:
            raise ValidationError(
                self.error_messages['invalid_date'],
                code='invalid_date',
                params={'value': value},
            )

        raise ValidationError(
            self.error_messages['invalid'],
            code='invalid',
            params={'value': value},
        )


class YourModel(models.Model):
    date = NepaliCalendar()

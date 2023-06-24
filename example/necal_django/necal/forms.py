import sys
from os import path

from django import forms
from django.core.exceptions import ValidationError
# sys.path.append(path.join(path.dirname(__file__), '../necal_py'))
sys.path.append('..')

from necal_py import bs


class NepaliDateInput(forms.DateInput):
    input_type = 'nepali-calendar'

    def get_context(self, name, value, attrs):
        if isinstance(value, str):
            try:
                year, month, day = (int(i) for i in value.split('-'))
                bs.date(year, month, day)
            except (ValueError, TypeError):
                value = None
        return super().get_context(name, value, attrs)


class NepaliDateField(forms.DateField):
    widget = NepaliDateInput

    def to_python(self, value):
        if value in self.empty_values:
            return None
        try:
            year, month, day = (int(i) for i in value.split('-'))
            nepali_date = bs.date(year, month, day)
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return nepali_date

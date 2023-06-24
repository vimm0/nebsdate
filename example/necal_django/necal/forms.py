from django import forms
from django.core.exceptions import ValidationError
from ...necal_py import bs


class NepaliDateInput(forms.DateInput):
    input_type = 'nepali-date'


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

from django.db import models
from django.db.models import fields


class NepaliCalendar(models.DateField):
    # Add source/link for field customization
    description = "Nepali Calendar Field"

    def formfield(self, **kwargs):
        pass

    def from_db_value(self, value, expression, connection):
        pass

    def get_prep_value(self, value):
        pass

    def to_python(self):
        pass
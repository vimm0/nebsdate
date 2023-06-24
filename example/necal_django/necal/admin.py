from django.contrib import admin

from necal.models import YourModel


@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    pass

# Generated by Django 4.2.2 on 2023-06-25 01:49

from django.db import migrations, models
import necal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', necal.models.NepaliCalendar()),
            ],
        ),
    ]

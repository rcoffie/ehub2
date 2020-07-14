# Generated by Django 3.0.7 on 2020-07-14 16:58

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20200714_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='brand',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20200705_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.CharField(choices=[('Mobile Phones', 'Mobile Phones'), ('Mobile Phone Accessories', 'Mobile Phone Accessories'), ('Computer Accessories', 'Computer Accessories'), ('TVs', 'TVs'), ('TV & Video Accessories', 'TV & Video Accessories'), ('Cameras & Camcorders', 'Cameras & Camcorders'), ('Audio & MP3', 'Audio & MP3'), ('Other Electronics', 'Other Electronics')], max_length=200, null=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-13 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image',
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-21 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0043_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
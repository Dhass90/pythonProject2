# Generated by Django 4.2.2 on 2023-06-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0036_alter_course_fees_fees_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_fees',
            name='fees_type',
            field=models.CharField(choices=[('Registration', 'Registration'), ('one_times', 'One Time'), ('two_times', 'Two Times'), ('three_times', 'Three Times')], max_length=50, null=True),
        ),
    ]

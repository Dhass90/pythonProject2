# Generated by Django 4.2.1 on 2023-05-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_remove_student_gender_student_gender_delete_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student", name="mobile", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="static/img"),
        ),
        migrations.AlterField(
            model_name="student", name="pincode", field=models.IntegerField(),
        ),
    ]
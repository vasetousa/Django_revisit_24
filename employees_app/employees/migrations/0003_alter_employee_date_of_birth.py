# Generated by Django 4.0.2 on 2024-02-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_date_of_birth_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]

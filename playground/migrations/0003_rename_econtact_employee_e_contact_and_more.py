# Generated by Django 4.0.6 on 2022-07-30 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_rename_econtact_employee_econtact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eContact',
            new_name='e_contact',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='eId',
            new_name='e_id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='eName',
            new_name='e_name',
        ),
    ]

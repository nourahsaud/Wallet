# Generated by Django 4.0.5 on 2022-06-14 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0004_rename_descriptions_expense_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='Descriptions',
            new_name='Description',
        ),
    ]

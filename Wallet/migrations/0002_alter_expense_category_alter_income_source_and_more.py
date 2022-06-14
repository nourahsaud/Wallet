# Generated by Django 4.0.5 on 2022-06-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='Category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='income',
            name='Source',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]
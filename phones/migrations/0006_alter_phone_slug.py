# Generated by Django 4.1.3 on 2022-12-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_alter_phone_lte_exists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.CharField(max_length=200),
        ),
    ]

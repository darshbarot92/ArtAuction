# Generated by Django 5.1.7 on 2025-04-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artglarry', '0011_alter_art_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sold',
            name='city',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sold',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sold',
            name='state',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

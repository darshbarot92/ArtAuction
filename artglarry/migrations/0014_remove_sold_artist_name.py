# Generated by Django 5.1.7 on 2025-04-20 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artglarry', '0013_alter_sold_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sold',
            name='artist_name',
        ),
    ]

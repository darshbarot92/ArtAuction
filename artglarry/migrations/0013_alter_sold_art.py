# Generated by Django 5.1.7 on 2025-04-20 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artglarry', '0012_alter_sold_address_alter_sold_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='artglarry.art'),
        ),
    ]

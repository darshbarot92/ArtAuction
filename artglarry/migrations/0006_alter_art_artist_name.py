# Generated by Django 5.1.7 on 2025-03-25 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artglarry', '0005_alter_user_bid_artist_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='artist_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='artglarry.atist_register'),
        ),
    ]

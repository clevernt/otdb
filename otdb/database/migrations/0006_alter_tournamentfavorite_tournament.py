# Generated by Django 5.0.6 on 2024-09-14 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_tournamentinvolvement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentfavorite',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_connections', to='database.tournament'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-08-07 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magas', '0011_players_in_current_game_approved_to_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='created_sessions',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
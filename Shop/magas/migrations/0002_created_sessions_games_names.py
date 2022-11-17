# Generated by Django 4.0.5 on 2022-08-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='created_sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masters_name', models.CharField(max_length=255)),
                ('number_of_players', models.IntegerField()),
                ('current_number_of_players', models.IntegerField()),
                ('description', models.TextField()),
                ('game_type', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='games_names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]

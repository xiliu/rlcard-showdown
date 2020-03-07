# Generated by Django 3.0.3 on 2020-02-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0004_auto_20200220_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamesPlayed', models.IntegerField()),
                ('winRate', models.DecimalField(decimal_places=3, max_digits=3)),
                ('gamesWon', models.IntegerField()),
                ('opponent', models.CharField(max_length=100)),
                ('agentID', models.CharField(max_length=100)),
                ('totalGamesPlayed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameID', models.IntegerField()),
                ('replayID', models.IntegerField()),
                ('replayLink', models.CharField(max_length=100)),
            ],
        ),
    ]
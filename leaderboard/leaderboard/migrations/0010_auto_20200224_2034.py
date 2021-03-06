# Generated by Django 3.0.3 on 2020-02-24 20:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0009_auto_20200224_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='opponent',
        ),
        migrations.AddField(
            model_name='agent',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agentID',
            field=models.CharField(default=uuid.UUID('23a054be-5119-44f7-b770-60556c8767e4'), max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameID',
            field=models.CharField(default=uuid.UUID('f524b126-2ee6-4a5d-ab4a-02af1bbd5347'), max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='replayID',
            field=models.CharField(default=uuid.UUID('f5003307-246e-473c-b9d4-fc814c832a1a'), max_length=100, unique=True),
        ),
    ]

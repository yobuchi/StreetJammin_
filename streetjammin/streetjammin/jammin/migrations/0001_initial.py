# Generated by Django 3.0 on 2019-12-08 00:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('mid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('mid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('sid', models.BigIntegerField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('dl_count', models.PositiveIntegerField()),
                ('last_dl', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('mid', 'sid')},
            },
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('sid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('did', models.BigIntegerField()),
                ('state', models.BooleanField(default=False)),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jammin.Musician')),
            ],
            options={
                'unique_together': {('sid', 'did')},
            },
        ),
    ]

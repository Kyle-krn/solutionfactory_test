# Generated by Django 4.0.6 on 2022-07-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('filter', models.JSONField()),
                ('datetime_start', models.DateTimeField()),
                ('datetime_end', models.DateTimeField()),
            ],
            options={
                'db_table': 'mailing',
            },
        ),
    ]

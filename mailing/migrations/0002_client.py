# Generated by Django 4.0.6 on 2022-07-27 13:09

from django.db import migrations, models
import mailing.models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=11, validators=[mailing.models.validate_number])),
                ('phone_code', models.IntegerField()),
                ('tag', models.TextField()),
                ('tz', timezone_field.fields.TimeZoneField(use_pytz=True)),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]

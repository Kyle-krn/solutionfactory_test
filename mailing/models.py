from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from timezone_field import TimeZoneField

# Create your models here.
class Mailing(models.Model):
    id = models.UUIDField(primary_key=True)
    text = models.TextField()
    filter = models.JSONField()
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()

    class Meta:
        db_table = "mailing"


def validate_number(value: str):
    if value[0] != '7':
        raise ValidationError(
            _('Номер должен начинаться с 7.'),
            params={'value': value},
        )
    if value.isdigit() is False:
        raise ValidationError(
            _('Номер должен состоять только из цифр.'),
            params={'value': value},
        )

class Client(models.Model):
    id = models.UUIDField(primary_key=True)
    phone_number = models.CharField(max_length=11 ,validators=[validate_number])
    phone_code = models.IntegerField()
    tag = models.TextField()
    tz = TimeZoneField(use_pytz=True)

    class Meta:
        db_table = "client"


    def save(self, *args, **kwargs):
        self.phone_code = int(self.phone_number[1:4])
        return super(Client, self).save(*args, **kwargs)


class Message(models.Model):
    id = models.UUIDField(primary_key=True)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=30)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = "message"
    

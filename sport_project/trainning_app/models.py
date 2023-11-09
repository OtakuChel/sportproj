from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
from users.forms import User


class BodySize(models.Model):
    date = models.DateField(verbose_name='Дата', null=True)
    biceps = models.PositiveIntegerField(verbose_name="Обхват бицепса", blank=True, null=True)
    breast = models.PositiveIntegerField(verbose_name="Обхват груди", blank=True, null=True)
    waist = models.PositiveIntegerField(verbose_name="Обхват талии", blank=True, null=True)
    buttocks = models.PositiveIntegerField(verbose_name="Обхват ягодиц", blank=True, null=True)
    hip = models.PositiveIntegerField(verbose_name="Обхват бедра", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
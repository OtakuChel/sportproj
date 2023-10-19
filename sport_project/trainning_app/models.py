from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class BodySize(models.Model):
    day = models.PositiveIntegerField(verbose_name='День', validators=[MinValueValidator(0),
                                       MaxValueValidator(31)])
    month = models.CharField(verbose_name='Месяц', max_length=10)
    biceps = models.PositiveIntegerField(verbose_name="Обхват бицепса", blank=True, null=True)
    breast = models.PositiveIntegerField(verbose_name="Обхват груди", blank=True, null=True)
    waist = models.PositiveIntegerField(verbose_name="Обхват талии", blank=True, null=True)
    buttocks = models.PositiveIntegerField(verbose_name="Обхват ягодиц", blank=True, null=True)
    hip = models.PositiveIntegerField(verbose_name="Обхват бедра", blank=True, null=True)
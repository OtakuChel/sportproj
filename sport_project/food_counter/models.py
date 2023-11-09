from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
from users.models import User


class EatingDate(models.Model):

    date = models.DateField(verbose_name='Дата', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        #print('str')
        return f'{self.__dict__["date"]}'

    def __repr__(self):
        #print('repr')
        return f'{self.__dict__["id"]}'

class Eating(models.Model):
    eating = models.CharField(verbose_name='Прием пищи', max_length=20)
    dish_1 = models.CharField(verbose_name='Блюдо №1', max_length=20)
    weight_1 = models.PositiveIntegerField(verbose_name='Граммовка блюда №1', validators=[MinValueValidator(1)])
    dish_2 = models.CharField(verbose_name='Блюдо №2', max_length=20, blank=True, null=True)
    weight_2 = models.PositiveIntegerField(verbose_name='Граммовка блюда №2', validators=[MinValueValidator(1)], blank=True, null=True)
    dish_3 = models.CharField(verbose_name='Блюдо №3', max_length=20, blank=True, null=True)
    weight_3 = models.PositiveIntegerField(verbose_name='Граммовка блюда №3', validators=[MinValueValidator(1)], blank=True, null=True)
    dish_4 = models.CharField(verbose_name='Блюдо №4', max_length=20, blank=True, null=True)
    weight_4 = models.PositiveIntegerField(verbose_name='Граммовка блюда №4', validators=[MinValueValidator(1)], blank=True, null=True)
    dish_5 = models.CharField(verbose_name='Блюдо №5', max_length=20, blank=True, null=True)
    weight_5 = models.PositiveIntegerField(verbose_name='Граммовка блюда №5', validators=[MinValueValidator(1)], blank=True, null=True)
    dish_6 = models.CharField(verbose_name='Блюдо №6', max_length=20, blank=True, null=True)
    weight_6 = models.PositiveIntegerField(verbose_name='Граммовка блюда №6', validators=[MinValueValidator(1)], blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.ForeignKey(EatingDate, on_delete=models.CASCADE, null=True, blank=True)
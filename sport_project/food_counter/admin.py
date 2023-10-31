from django.contrib import admin
from .models import EatingDate, Eating


# Register your models here.


@admin.register(EatingDate)
class bd1Admin(admin.ModelAdmin):
    list_display = ['date']

@admin.register(Eating)
class bd2Admin(admin.ModelAdmin):
    list_display = ['eating', 'date']
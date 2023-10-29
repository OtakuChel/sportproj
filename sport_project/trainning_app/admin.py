from django.contrib import admin
from .models import BodySize
# Register your models here.


@admin.register(BodySize)
class BodySizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'date']

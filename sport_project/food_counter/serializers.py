from rest_framework import serializers

from .models import EatingDate, Eating


class EatingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EatingDate
        fields = ('date', 'user')

class EatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eating
        fields = ('date', 'eating')
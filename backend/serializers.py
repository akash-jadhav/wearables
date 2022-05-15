from dataclasses import fields
import json

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import VitalData


class VitalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalData
        fields = '__all__'

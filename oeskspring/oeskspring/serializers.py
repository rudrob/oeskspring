from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

    def validate(self, data):
        if data['capacity'] <= 0:
            raise serializers.ValidationError("Capacity must be greater than 0")
        return data


########
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

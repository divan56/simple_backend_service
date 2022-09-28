from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'course', 'college', 'date_of_birth', 'studies_from']




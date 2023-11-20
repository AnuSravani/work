from rest_framework import serializers
from .models import Roberts,RobertCategorys,Manufacturers
from django.contrib.auth.models import User


class RobertCategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=RobertCategorys
        fields="__all__"


class ManufactureSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Manufacturers
        fields="__all__"

        

class RobertSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    manufacture_date=serializers.DateField(read_only=True)
    robert_cate_name=serializers.CharField(read_only=True)
    manufacture_name=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Roberts
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["username","password","email","id"]

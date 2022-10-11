from importlib.metadata import files
from rest_framework import serializers
from .models import *
from customer.models import *



class CountrySerialization(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields="__all__"

class StateSerialization(serializers.ModelSerializer):
    class Meta:
        model=State
        fields="__all__"


class DistricSerialization(serializers.ModelSerializer):
    class Meta:
        model=Distric
        fields="__all__"

class PincodeSerialization(serializers.ModelSerializer):
    class Meta:
        model=Pincode
        fields="__all__"


class GenderSerialization(serializers.ModelSerializer):
    class Meta:
        model=Gender
        fields="__all__"


class CustomerSerialization(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class ReferralSerialization(serializers.ModelSerializer):
    class Meta:
        model=Referral
        fields="__all__"


class TestSelialiaztion(serializers.ModelSerializer):
    class Meta:
        model=Test
        fields="__all__"
class TestSelialiaztion_ser(serializers.Serializer):
    test=TestSelialiaztion()

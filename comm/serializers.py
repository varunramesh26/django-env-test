from dataclasses import field
from operator import mod
from pyexpat import model
from rest_framework import serializers
from .models import FarmerInfo

class FarmerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerInfo
        fields = ['name', 'village', 'crop']

# class FarmerInfoSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     village = serializers.CharField(max_length=255)
#     crop = serializers.CharField(max_length=255)

#     def create(self, validated_data):
#         return FarmerInfo.objects.create(** validated_data)

#     def upate(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.village = validated_data.get('village', instance.village)
#         instance.crop = validated_data.get('crop', instance.crop)
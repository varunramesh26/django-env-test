from difflib import restore
from http.client import ImproperConnectionState
import imp
# from subprocess import ABOVE_NORMAL_PRIORITY_CLASS
from sys import api_version
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FarmerInfo
from .serializers import FarmerInfoSerializer
from . import serializers

# @api_view(['GET', 'POST'])
# def farmerinfo_list(request):
#     if request.method == 'GET':
#         farmerinfo = FarmerInfo.objects.all()
#         serializer = FarmerInfoSerializer(farmerinfo, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = FarmerInfoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT'])
# def farmerinfo_detail(request, pk):
#     farmerinfo = FarmerInfo.objects.get(pk=pk)

#     if request.method == 'GET':
#         serializer = FarmerInfoSerializer(farmerinfo)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = FarmerInfoSerializer(farmerinfo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FarmerInfoList(APIView):
    def get(self, request):
        farmerinfo = FarmerInfo.objects.all()
        serializer = FarmerInfoSerializer(farmerinfo, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from picwithmodel.models import Imageformodel
from picwithmodel.serializers import ImageformodelSerializer
from rest_framework import status

class ImageformodelList(APIView):
    def get(self,request):
        imageformodel_obj=Imageformodel.objects.all()
        serializer=ImageformodelSerializer(imageformodel_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ImageformodelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
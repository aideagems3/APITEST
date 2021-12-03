from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from picwithmodel.models import Imageformodel
from picwithmodel.serializers import ImageformodelSerializer
from rest_framework import status
from django.http import HttpResponse



from .utils import *
from picwithmodel.darknet import darknet

class ImageformodelList(APIView):

    def get(self,request):
    
        imageformodel_obj=Imageformodel.objects.all()
        serializer=ImageformodelSerializer(imageformodel_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        
        if request.POST.get("Imagefromuser", None) is not None:
            serializer=ImageformodelSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                # print("your serializer=",serializer.data)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            pass

class ImageformodelDetail(APIView):

     def get(self,request,pk):
        try:
            imageformodel_obj=Imageformodel.objects.get(pk=pk)
        except:
            return Response({'error': 'Page Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=ImageformodelSerializer(imageformodel_obj)
        return Response(serializer.data)

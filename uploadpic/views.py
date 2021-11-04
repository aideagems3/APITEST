from inspect import ismemberdescriptor
from django.http.response import JsonResponse
from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from uploadpic.models import Voltage,Equipment,Sub_equipment,Abnormal,Job_upload
from uploadpic.serializers import VoltageSerializer,EquipmentSerializer,Sub_equipmentSerializer,AbnormalSerializer,Job_uploadSerializer
from rest_framework import status

import os
from PIL import  Image
from PIL.ExifTags import  TAGS

# def test_json(request):
#     data = list()
#     for i in Job_upload.objects.all():
#         data.append({'job_date':str(i.job_date),
#                     'job_officerid':i.job_officerid.id, 
#                     'job_picture':i.job_picture,
#                     'subeq_name':i.subeq_name.id,
#                     'abnor_name':i.abnor_name.id,
#                     'abnor_other':i.abnor_other,
#                     })
#     return HttpResponse(json.dumps(data))


# def testjson(request):
#     vol_obj = Voltage.objects.all()
#     vol_dict = {
#         'vol_name': list(vol_obj.values()) 
#     }
#     return JsonResponse(vol_dict)
# def testjson(request):

# def testjson(request):
#     myobj = Job_upload.objects.all().values()
#     print("Test Value All Element")
#     print(myobj)

# def testjson_detail(request,pk):
#     each_obj = Job_upload.objects.get(pk=pk)
#     p_dict = {
#         'job_date':each_obj.job_date,
#         'job_time': each_obj.job_time,
#         'job_officerid': each_obj.job_officerid.id,
#         'job_picture': each_obj.job_picture,
#         'subeq_name': each_obj.subeq_name.id,
#         'abnor_name': list(each_obj.abnor_name.values()),
#         'abnor_other': each_obj.abnor_other,
#     }
#     return JsonResponse(p_dict)
    
def reqresjson(request):
    return render(request,"uploadpic/reqresjson.html")
    
def mypostapi(request):
    return render(request,"uploadpic/mypostapi.html")

class VoltageList(APIView):
    def get(self,request):
        vol_obj=Voltage.objects.all()
        serializer=VoltageSerializer(vol_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=VoltageSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class VoltageDetial(APIView):

    def get(self,request,pk):
        try:
            vol_obj=Voltage.objects.get(pk=pk)
        except:
            return Response({'error': 'Page Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=VoltageSerializer(vol_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        vol_obj=Voltage.objects.get(pk=pk)
        serializer=VoltageSerializer(vol_obj,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        vol_obj=Voltage.objects.get(pk=pk)
        vol_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EquipmentList(APIView):
    def get(self,request):
        eq_obj=Equipment.objects.all()
        serializer=EquipmentSerializer(eq_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=EquipmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EquipmentDetial(APIView):

    def get(self,request,pk):
        try:
            eq_obj=Equipment.objects.get(pk=pk)
        except:
            return Response({'error': 'Page Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=EquipmentSerializer(eq_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        eq_obj=Equipment.objects.get(pk=pk)
        serializer=EquipmentSerializer(eq_obj,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        eq_obj=Equipment.objects.get(pk=pk)
        eq_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Sub_equipmentList(APIView):
    def get(self,request):
        sub_eq_obj=Sub_equipment.objects.all()
        serializer=Sub_equipmentSerializer(sub_eq_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Sub_equipmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Sub_equipmentDetial(APIView):

    def get(self,request,pk):
        try:
            sub_eq_obj=Sub_equipment.objects.get(pk=pk)
        except:
            return Response({'error': 'Page Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=Sub_equipmentSerializer(sub_eq_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        sub_eq_obj=Sub_equipment.objects.get(pk=pk)
        serializer=Sub_equipmentSerializer(sub_eq_obj,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        sub_eq_obj=Sub_equipment.objects.get(pk=pk)
        sub_eq_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AbnormalList(APIView):
    def get(self,request):
        abnor_obj=Abnormal.objects.all()
        serializer=AbnormalSerializer(abnor_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=AbnormalSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AbnormalDetial(APIView):

    def get(self,request,pk):
        try:
            abnor_obj=Abnormal.objects.get(pk=pk)
        except:
            return Response({'error': 'Page Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=AbnormalSerializer(abnor_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        abnor_obj=Abnormal.objects.get(pk=pk)
        serializer=AbnormalSerializer(abnor_obj,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        abnor_obj=Abnormal.objects.get(pk=pk)
        abnor_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Job_uploadList(APIView):
    def get(self,request):
        job_upload_obj=Job_upload.objects.all()
        serializer=Job_uploadSerializer(job_upload_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Job_uploadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Job_uploadDetial(APIView):

    def get(self,request,pk):
        try:
            job_upload_obj=Job_upload.objects.get(pk=pk)
        except:
            return Response({'error': 'Page Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=Job_uploadSerializer(job_upload_obj)
        return Response(serializer.data)
    
    def delete(self,request,pk):
        job_upload_obj=Job_upload.objects.get(pk=pk)
        job_upload_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










    








from django.shortcuts import render
import json
from django.http import HttpResponse
from uploadpic.models import Job_upload 
from rest_framework import generics
from uploadpic.models import Voltage,Equipment,Sub_equipment,Abnormal,Job_upload
from uploadpic.serializers import VoltageSerializer,EquipmentSerializer,Sub_equipmentSerializer,AbnormalSerializer,Job_uploadSerializer

#P'First
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,)
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

# class VoltageGenericsView(generics.ListCreateAPIView): 
#         queryset= Voltage.objects.all()
#         serializer_class=VoltageSerializer

@api_view(['GET'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def voltage(request):

    return Response({'voltage_name':'777'})

class EquipmentGenericsView(generics.ListCreateAPIView): 
        queryset= Equipment.objects.all()
        serializer_class=EquipmentSerializer

class Sub_equipmentGenericsView(generics.ListCreateAPIView): 
        queryset= Sub_equipment.objects.all()
        serializer_class=Sub_equipmentSerializer

class AbnormalGenericsView(generics.ListCreateAPIView): 
        queryset= Abnormal.objects.all()
        serializer_class=AbnormalSerializer

class Job_uploadGenericsView(generics.ListCreateAPIView): 
        queryset= Job_upload.objects.all()
        serializer_class=Job_uploadSerializer #ไม่ต้องเขียนviews.py

def testjson(request):
    return render(request,"uploadpic/testjson.html")

def reqresjson(request):
    return render(request,"uploadpic/reqresjson.html")
    
def mypostapi(request):
    return render(request,"uploadpic/mypostapi.html")


@api_view(['POST'])
@permission_classes((AllowAny,))
def uploadSometing(request):
    # save model

    return Response({'text':'upload success'})


from uploadpic.models import Job_upload, Sub_equipment

@api_view(['GET'])
@permission_classes((AllowAny,))
def readSomething(request):
    # read model
    jobs = Job_upload.objects.all()
    result=[]

    for job in jobs:
        print(job.__dict__)
        subEquipment=Sub_equipment.objects.get(id = job.subeq_name_id)
        print(subEquipment.__dict__)
        equipment = Equipment.objects.get(id=subEquipment.eq_name_id)
        print(equipment.__dict__)
        result.append({'jobId':job.id,'equipment':equipment.Eq_name, 
            'subEquipment':subEquipment.Subeq_name})
    




    
    return Response({'data':result})
    








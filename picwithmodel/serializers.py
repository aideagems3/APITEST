from rest_framework import serializers
from django.contrib.auth import get_user_model
from picwithmodel.models import  Imageformodel
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
import base64,uuid,io
import numpy as np
from base64 import b64decode
from PIL import Image

class Base64ImageField(serializers.ImageField):

    # # Convert Base64 to Image
    # def to_internal_value(self,data):
    #     # print('data',data)
    #     _format,str_img = data.split(';base64')
    #     decoded_file = base64.b64decode(str_img)
    #     fname = f"{str(uuid.uuid4())[:10]}.JPEG"
    #     # print('format',_format)
    #     # print('str_img',str_img)
    #     # print('type str_img' ,type(str_img))
    #     # print('decoded_file',decoded_file)
    #     # print('fname',fname)
    #     data = ContentFile(decoded_file,name=fname)
    #     return super().to_internal_value(data)

    def to_internal_value(self,data):
  
        base64_data = data.split(',', 1)[1]
        decoded_file = base64.b64decode(base64_data)
        buff = io.BytesIO(decoded_file)
        fname = f"{str(uuid.uuid4())[:10]}.JPEG"
        # print("buff=",buff)
        data = ImageFile(buff,name=fname)
        # print("data=",data)
        return super().to_internal_value(data)
        

 

class ImageformodelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Imagefromuser = Base64ImageField()
    Objects = serializers.CharField()
    Success = serializers.BooleanField()
    Time = serializers.CharField()
    # Boxespic = serializers.ImageField()
    
    def create(self,validated_data):
        return Imageformodel.objects.create(**validated_data)

 


     
        
      
     
 


    



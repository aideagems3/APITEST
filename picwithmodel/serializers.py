from rest_framework import serializers
from django.contrib.auth import get_user_model
from picwithmodel.models import  Imageformodel



class ImageformodelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Imagefromuser = serializers.ImageField()
    Equipmentfromuser = serializers.CharField()
    
    
    def create(self,validated_data):
        return Imageformodel.objects.create(**validated_data)

 


     
        
      
     
 


    



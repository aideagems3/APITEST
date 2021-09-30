from rest_framework import serializers
from django.contrib.auth import get_user_model
from uploadpic.models import  Voltage,Equipment,Sub_equipment,Abnormal,Job_upload

officerid = get_user_model()

class VoltageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Volt_name = serializers.CharField()
    subeq_volt_list = serializers.StringRelatedField(many=True,read_only=True)
    

    def create(self,validated_data):
        return Voltage.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Volt_name = validated_data.get('Volt_name', instance.Volt_name)
        instance.save()
        return instance

class EquipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Eq_name = serializers.CharField()
    subeq_eq_list = serializers.StringRelatedField(many=True,read_only=True)
    def create(self,validated_data):
        return Equipment.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Eq_name = validated_data.get('Eq_name', instance.Eq_name)
        instance.save()
        return instance

class Sub_equipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Subeq_name = serializers.CharField()
    volt_name = serializers.PrimaryKeyRelatedField(queryset=Voltage.objects.all())
    eq_name = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all())
    
    def create(self,validated_data):
        return Sub_equipment.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Subeq_name = validated_data.get('Subeq_name', instance.Subeq_name)
        instance.save()
        return instance
    
class AbnormalSerializer(serializers.Serializer):
    id = serializers.IntegerField() #use this id
    Abnor_name = serializers.CharField()

    def create(self,validated_data):
        return Abnormal.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.Abnor_name = validated_data.get('Abnor_name', instance.Abnor_name)
        instance.save()
        return instance     

class Job_uploadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    job_date = serializers.DateField()
    job_time = serializers.TimeField()
    job_officerid = serializers.PrimaryKeyRelatedField(queryset=officerid.objects.all())
    job_picture = serializers.URLField()
    subeq_name = serializers.PrimaryKeyRelatedField(queryset=Sub_equipment.objects.all())
    abnor_name = AbnormalSerializer(many=True)
    abnor_other = serializers.CharField()
    
 
    def create(self, validated_data):
        abnor_name = validated_data.pop('abnor_name') 
        job_upload = Job_upload.objects.create(**validated_data) 
        
        # for s in abnor_name:
        #     each_abnor_obj=Abnormal.objects.filter(id__in=[s['id']])
        #     job_upload.abnor_name.set(each_abnor_obj)
        #     print(job_upload.abnor_name.values())   
            
        job_upload.abnor_name.set(Abnormal.objects.filter(id__in=[s['id'] for s in abnor_name]))
        return job_upload
        
     
        
      
     
 


    



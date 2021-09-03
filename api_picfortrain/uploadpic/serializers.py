from rest_framework import serializers
from django.contrib.auth import get_user_model
from uploadpic.models import Voltage,Equipment,Sub_equipment,Abnormal,Job_upload

officerid = get_user_model()

class officeridSerializer(serializers.ModelSerializer):
    class Meta:
        model = officerid
        fields = ['id','first_name','last_name']

class VoltageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voltage
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class Sub_equipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_equipment
        fields = '__all__'

class AbnormalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abnormal
        fields = '__all__'

class Job_uploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_upload
        fields = '__all__'
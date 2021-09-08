from django.contrib import admin
from uploadpic.models import Voltage,Equipment,Sub_equipment,Abnormal,Job_upload

admin.site.register(Voltage)
admin.site.register(Equipment)
admin.site.register(Sub_equipment)
admin.site.register(Abnormal)
admin.site.register(Job_upload)
# @admin.register(Voltage)
# class VoltageAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Equipment)
# class EquipmentAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Sub_equipment)
# class Sub_equipmentAdmin(admin.ModelAdmin):
#     list_display = ['Subeq_name','volt_name','eq_name']

# @admin.register(Abnormal)
# class AbnormalAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Job_upload)
# class Job_uploadAdmin(admin.ModelAdmin):
#     list_display = ['job_date','job_time','job_officerid','job_picture','subeq_name','get_abnor_name','abnor_other']

     
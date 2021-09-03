from django.contrib import admin
from uploadpic import models

@admin.register(models.Voltage)
class VoltageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Sub_equipment)
class Sub_equipmentAdmin(admin.ModelAdmin):
    list_display = ['Subeq_name','volt_name','eq_name','eq_name2','eq_name3']

@admin.register(models.Abnormal)
class AbnormalAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Job_upload)
class Job_uploadAdmin(admin.ModelAdmin):
    list_display = ['job_date','job_time','job_officerid',
                    'job_picture','subeq_name','abnor_name','abnor_other','subeq_name2','abnor_name2','abnor_other2','subeq_name3','abnor_name3','abnor_other3']

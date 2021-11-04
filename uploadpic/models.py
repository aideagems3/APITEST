from django.db import models
from django.contrib.auth import get_user_model

officerid = get_user_model()


class Voltage(models.Model):
    Volt_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Volt_name

class Equipment(models.Model):
    Eq_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Eq_name

class Sub_equipment(models.Model):
    Subeq_name = models.CharField(max_length=100)
    volt_name = models.ForeignKey(Voltage,related_name='subeq_volt_list',on_delete=models.CASCADE)
    eq_name = models.ForeignKey(Equipment,related_name='subeq_eq_list',on_delete=models.CASCADE)
 
    def __str__(self):
        return self.Subeq_name
    

class Abnormal(models.Model):
    Abnor_name = models.CharField(max_length=100)
    def __str__(self):
        return self.Abnor_name

class Job_upload(models.Model):
    
    job_date = models.DateField(auto_now_add=True)
    job_time = models.TimeField(auto_now_add=True)
    job_officerid = models.ForeignKey(officerid,on_delete=models.CASCADE)
    job_picture = models.URLField(max_length=500)
    subeq_name = models.ForeignKey(Sub_equipment,on_delete=models.CASCADE)
    abnor_name = models.ManyToManyField(Abnormal)
    abnor_other = models.CharField(max_length=100,blank=True,null=True)

   
        

   







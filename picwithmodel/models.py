from django.db import models

def Uploadpath(instance,filename):
    return '/'.join(['Equipment',str(instance.Equipmentfromuser),filename])

class Imageformodel(models.Model):
    Imagefromuser = models.ImageField(upload_to=Uploadpath)
    Equipmentfromuser = models.CharField(max_length=100)

    def __str__(self):
        return self.Equipmentfromuser

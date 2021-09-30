from django.db import models
from PIL import Image
import io
import base64
import numpy as np
from numpy.lib import financial
from .utils import *
from .Darknet import DarkNet
import cv2



def Uploadpath(instance,filename):
    return '/'.join(['Media',filename])

def detection(original_image, web=True):
        cfg_file = './yolov3_Tuned.cfg'
        weight_file = './yolov3.weights'
        names = './coco.names'
        # Dartnet.py
        m = DarkNet(cfg_file)
        m.load_weights(weight_file)
        # utils.py
        class_names = load_coco_names(names) 

        resized_image = cv2.resize(np.float32(original_image), (m.width, m.height))
        nms_thresh = 0.018
        iou_thresh = 0.2
        # utils.py
        boxes, detection_time = detect_objects(m, resized_image, iou_thresh, nms_thresh)
        objects = label_objects(boxes, class_names)

        if web:
            # utils.py
            plot_object_boxes(original_image, boxes, class_names)
           
        return objects, detection_time

class Imageformodel(models.Model):
    Imagefromuser = models.ImageField(upload_to=Uploadpath)
    Objects = models.CharField(max_length=200,blank=True,null=True)
    Success = models.BooleanField(default=False,blank=True,null=True)
    Time = models.CharField(max_length=20,blank=True,null=True)
    # Boxespic = models.ImageField(blank=True,null=True)
    def save(self,*args,**kwargs):
        
        # Base64 for image processing

        # print("Input in models=",self.Imagefromuser)
        data = np.array(Image.open(self.Imagefromuser))
        # print("open in models=",data)
        result, detection_time = detection(data)
        # print("result=",result)
        # print("detection_time=",detection_time)

       
        if result:
            self.Success = True
        else:
            self.Success = False
        self.Time = str(round(detection_time))+" seconds"
        self.Objects = result
       
        # print("self.Success=",self.Success)
        # print("self.Time=",self.Time)
        # print("self.Time=",self.Objects)
        
        super(Imageformodel,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

       
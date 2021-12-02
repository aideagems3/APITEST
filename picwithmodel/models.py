from django.db import models
from PIL import Image
from numpy.lib import financial

import cv2
import os
import numpy as np
from base64 import b64decode
import base64,uuid,io
from picwithmodel.darknet.darknet_images import image_detection
from picwithmodel.darknet.darknet import load_network
from matplotlib import pyplot as plt

from PIL.ExifTags import  TAGS

def Uploadpath(instance,filename):
    return '/'.join(['Media',filename])

# def detection(original_image, web=True):
#         cfg_file = './yolov3_Tuned.cfg'
#         weight_file = './yolov3.weights'
#         names = './coco.names'
#         # Dartnet.py
#         m = DarkNet(cfg_file)
#         m.load_weights(weight_file)
#         # utils.py
#         class_names = load_coco_names(names) 

#         resized_image = cv2.resize(np.float32(original_image), (m.width, m.height))
#         nms_thresh = 0.018
#         iou_thresh = 0.2
#         # utils.py
#         boxes, detection_time = detect_objects(m, resized_image, iou_thresh, nms_thresh)
#         objects = label_objects(boxes, class_names)

#         if web:
#             # utils.py
#             plot_object_boxes(original_image, boxes, class_names)
           
#         return objects, detection_time
def detection(original_image):
    print("current path=",os.getcwd())
    weights = './picwithmodel/darknet/weights/yolov3_insulator_train_4000.weights'
    # input = './MEDIA/Media/00003.jpg'
    datafile = './picwithmodel/darknet/data/insulator_data/insulator_data.data'
    cfg = './picwithmodel/darknet/cfg/yolov3_insulator_test.cfg'
    thresh= 0.5

    
    #calculate network =>darknet.py
    network, class_names, class_colors = load_network(cfg, datafile,  weights, 1)
    print("network=",network)
    print("class_names=",class_names)
    print("class_colors=",class_colors)

    # result plot image=> darknet_images.py +  ประมวลผล=>darknet.py
    image, detections,time_taken = image_detection(
                                        original_image, 
                                        network, 
                                        class_names, 
                                        class_colors, 
                                        thresh
                                        )       
    print("detection=",detections)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # plot & save picture
    plt.axis("off")
    fig = plt.gcf()
    fig.savefig("./picwithmodel/static/img/test.jpeg",dpi='figure',bbox_inches='tight')
    
    
    # show picture here
    # plt.show()

    return detections,time_taken

class Imageformodel(models.Model):
    Imagefromuser = models.ImageField(upload_to=Uploadpath)
    Objects = models.CharField(max_length=200,blank=True,null=True)
    Success = models.BooleanField(default=False,blank=True,null=True)
    Time = models.CharField(max_length=20,blank=True,null=True)
    Lat = models.CharField(max_length=20,blank=True,null=True)
    Lng = models.CharField(max_length=20,blank=True,null=True)

    
    def save(self,*args,**kwargs):

    #==================================================   
        # #Image to Lat Lng
        # image = Image.open(self.Imagefromuser)
        # exif={}
    #เขียนเงื่อนไขกรณ๊ ไม่มี gps ด้วยนะ
        # for tag,value in image._getexif().items():
        #     # print(tag,value)
        #     # check gps image(key) in gps TAGS(key)
        #     if tag in TAGS:
        #         exif[TAGS[tag]]=value
        # # print(exif)
        
        # if 'GPSInfo' in exif:
        #     latitude = '{0} {1} {2:.2f} {3}'.format(

        #         exif['GPSInfo'][2][0][0],
        #         exif['GPSInfo'][2][1][0],
        #         exif['GPSInfo'][2][2][0] / exif['GPSInfo'][2][2][1],
        #         exif['GPSInfo'][1]
                
        #     )
        #     self.Lat=latitude
        #     print("mylat=",latitude)

        #     longitude = '{0} {1} {2:.2f} {3}'.format(
        #         exif['GPSInfo'][4][0][0],
        #         exif['GPSInfo'][4][1][0],
        #         exif['GPSInfo'][4][2][0] / exif['GPSInfo'][4][2][1],
        #         exif['GPSInfo'][3]
        #     )
        #     self.Lng=longitude
        #     print("mylng=",longitude)

    #==================================================
        # Image for image processing
        # print("Input in models=",self.Imagefromuser)
        class_prob = {}

        data = np.array(Image.open(self.Imagefromuser))
        print("old data=",data)
        #swap last to first column for same as using imread(img_path)
        #accessing 3Darray=> array[dept][row][column] = array[:,:,column]
        #build 3Darray=> array[[[1,2],[3,4]],[[5,6],[7,8]]]

        data[:,:, [2, 0]] = data[:,:, [0, 2]]
        print("new data=",data)
        # print("open in models=",data)
        # result = detection(Image.open(self.Imagefromuser))
        result,detection_time = detection(data)
        print("result=",result)
        print("detection_time=",detection_time)
        
        
        for key,percent,thebox in result:
            print("key=",key)
            print("percent=",percent)
            print("thebox=",thebox)

            if key in class_prob:
                #append percent
                if not isinstance(class_prob[key], list):
                    class_prob[key] = [class_prob[key]]
                class_prob[key].append(percent)
                print("class_prob[key]=",class_prob[key])
                print("result1=",class_prob)
            else:
                #append percent
                class_prob[key] = percent
                print("result2=",class_prob)
            
        print("fianlresult=",class_prob)

        result = class_prob
        if result:
            self.Success = True
        else:
            self.Success = False
        self.Time = str(round(detection_time))+" seconds"
        self.Objects = result
       
        print("self.Success=",self.Success)
        print("self.Time=",self.Time)
        print("self.Objects=",self.Objects)
    #==================================================   
        super(Imageformodel,self).save(*args, **kwargs)

    
    def __str__(self):
        return str(self.id)

       
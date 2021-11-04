from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from picwithmodel.models import Imageformodel
from picwithmodel.serializers import ImageformodelSerializer
from rest_framework import status
from django.http import HttpResponse



from .utils import *
from picwithmodel.darknet import darknet

class ImageformodelList(APIView):

    def get(self,request):
    
        imageformodel_obj=Imageformodel.objects.all()
        serializer=ImageformodelSerializer(imageformodel_obj,many=True)
        return Response(serializer.data)

    def post(self,request):
        
        if request.POST.get("Imagefromuser", None) is not None:
            serializer=ImageformodelSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                # print("your serializer=",serializer.data)
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            pass

class ImageformodelDetail(APIView):

     def get(self,request,pk):
        try:
            imageformodel_obj=Imageformodel.objects.get(pk=pk)
        except:
            return Response({'error': 'Page Not Found'},status=status.HTTP_404_NOT_FOUND)

        serializer=ImageformodelSerializer(imageformodel_obj)
        return Response(serializer.data)



# final result= {'dog': 1, 'truck': 1, 'tvmonitor': 1, 'pottedplant': 1, 'person': 1}    
# {'success': True, 'time': '2 seconds', 'objects': {'dog': 1, 'truck': 1, 'tvmonitor': 1, 'pottedplant': 1, 'person': 1}}
# def testcustom(request):
    
    


  
# from picwithmodel.darknet.darknet_images import image_detection
# from picwithmodel.darknet import darknettest
# from picwithmodel.darknet import darknettest_images
# import cv2
# import numpy as np
# import random


# def detection(request):
    
#     input = r'D:\Gems#3\ProjectUploadPic\Upload_API\api_picfortrain\MEDIA\Media\00003.jpg'
#     class_names = r'D:\Gems#3\ProjectUploadPic\Upload_API\api_picfortrain\picwithmodel\darknet\data\trafficsign_data\classes.names'
#     network = darknettest.load_net(b"./picwithmodel/darknet/cfg/yolov3_custom_test.cfg", b"./picwithmodel/darknet/weights/yolov3_custom_train_best.weights", 0)
#     meta = darknettest.load_meta(b"./picwithmodel/darknet/data/trafficsign_data/custom_traffic.data")
#     r = darknettest.detect(network, meta,b'./MEDIA/Media/00003.jpg', 0.25)

#     print("network=",network)
#     print("meta=",meta)
#     print("after detect=",r)
    
#     im = darknettest.load_image(b'./MEDIA/Media/00003.jpg', 0, 0)
#     classify = darknettest.classify(network, meta, im)
#     print("classify=",classify)

#     darknettest_images.image_detection()

    #เอาส่วนที่ทำรูป darknet_images.py มาใส่
    # image, detections = image_detection(
    #                                     input, 
    #                                     network, 
    #                                     class_names, 
    #                                     class_color, 
    #                                     thresh
    #                                     )       
    # print("detection=",detections)

# import cv2
# import os
# import numpy as np
# from base64 import b64decode
# import base64,uuid,io
# from picwithmodel.darknet.darknet_images import image_detection
# from picwithmodel.darknet.darknet import load_network
# from matplotlib import pyplot as plt

# def detection(original_image, web=True):
#     weights = './picwithmodel/darknet/weights/yolov3_custom_train_best.weights'
#     input = './MEDIA/Media/00003.jpg'
#     datafile = './picwithmodel/darknet/data/trafficsign_data/custom_traffic.data'
#     cfg = './picwithmodel/darknet/cfg/yolov3_custom_test.cfg'
#     thresh= 0.5

    
#     #calculate network =>darknet.py
#     network, class_names, class_colors = load_network(cfg, datafile,  weights, 1)
#     print("network=",network)
#     print("class_names=",class_names)
#     print("class_colors=",class_colors)

#     # result plot image=> darknet_images.py +  ประมวลผล=>darknet.py
#     image, detections = image_detection(
#                                         input, 
#                                         network, 
#                                         class_names, 
#                                         class_colors, 
#                                         thresh
#                                         )       
#     print("detection=",detections)
#     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     # plot & save picture
#     plt.axis("off")
#     fig = plt.gcf()
#     fig.savefig("./picwithmodel/static/img/test.jpeg", dpi=360)
#     # show picture in website
#     # plt.show()



  


from django.shortcuts import *
from sightengine.client import SightengineClient
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.
#import try_karu as t
#import try_object_detect_karu as t_o
#,api_user,api_secret,image_path
#from try_karu import nudity_shodhuya
#from try_object_detect_karu import box_draw_karu


import tensorflow as tf 


def nudity_shodhuya(api_user,api_secret,image_path):

	execution_path = os.getcwd()
	print(execution_path)
	client = SightengineClient(api_user,api_secret)

	output = client.check('nudity').set_file(os.path.join(execution_path ,image_path))
	arr = []
	print(output)
	if output['status'] == 'success':
		raw = output['nudity']['raw']
		safe = output['nudity']['safe']
		partial = output['nudity']['partial']
		arr.append(raw)
		arr.append(safe)
		arr.append(partial)
	result = sorted(arr,reverse=True)[0]
	if result == raw or result == partial:
		return "Not safe="+str(result)
	else:
		return "Safe"+str(result)

	#return output

from imageai.Detection import ObjectDetection
import os

#image_path = "pic3.jpeg"
def box_draw_karu(image_path):
	execution_path = os.getcwd()
	print(execution_path)

	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image_path), output_image_path=os.path.join(execution_path , "output_"+image_path))

	for eachObject in detections:
	    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
	tf.keras.backend.clear_session()


api_user = '737578295'
api_secret = 'Us7NTD8APM2ZzUZJtiVA'
image_path = 'pic1.jpeg'

@csrf_protect
def render_karu(request):
	c={}
	execution_path = os.getcwd()
	print(execution_path)
	#text = "<h1> Response of Nudity:%s </h1>"%nudity_shodhuya(api_user,api_secret,image_path)
	print(request.method)
	if request.method == 'POST':
		image_path=request.POST['photo']
		print("image path")
		print(image_path)
		response1=nudity_shodhuya(api_user,api_secret,image_path)
		return render(request,'templates/main.html',{'response1':response1},c)
	else:
		#box_draw_karu(image_path)
		print("inside else")
		return render(request,os.path.join(execution_path ,'templates/test.html'),{},c)
	#return rrender(request,'templates/main.html',{'response1':response1},c)

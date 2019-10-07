# import numpy as np
# import os
# import six.moves.urllib as urllib
# import sys
# import tarfile
# import tensorflow as tf
# import zipfile

# from collections import defaultdict
# from io import StringIO
# from matplotlib import pyplot as plt
# from PIL import Image

# if tf.__version__ < '1.4.0':
#   raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')


# # This is needed to display the images.
# #%matplotlib inline

# # This is needed since the notebook is stored in the object_detection folder.
# sys.path.append("..")


# from utils import label_map_util

# from utils import visualization_utils as vis_util


# # What model to download.
# MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
# MODEL_FILE = MODEL_NAME + '.tar.gz'
# DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# # Path to frozen detection graph. This is the actual model that is used for the object detection.
# PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# # List of the strings that is used to add correct label for each box.
# PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

# NUM_CLASSES = 90

# opener = urllib.request.URLopener()
# opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
# tar_file = tarfile.open(MODEL_FILE)
# for file in tar_file.getmembers():
#   file_name = os.path.basename(file.name)
#   if 'frozen_inference_graph.pb' in file_name:
#     tar_file.extract(file, os.getcwd())



from imageai.Detection import ObjectDetection
import os

image_path = "pic3.jpeg"
def box_draw_karu(image_path):
	execution_path = os.getcwd()

	detector = ObjectDetection()
	detector.setModelTypeAsRetinaNet()
	detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image_path), output_image_path=os.path.join(execution_path , "output_"+image_path))

	for eachObject in detections:
	    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

box_draw_karu(image_path)







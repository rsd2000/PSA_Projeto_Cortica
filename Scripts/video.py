import os
import cv2
import time
import torch
from PIL import Image
import numpy as np

model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local') 
  
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image
# image
img = 'F:\vscode1\Camera_Flask_App\static\01.jpg'
# inference
results = model(img)
# inference with larger input size
results = model(img, size=1280)
# inference with test time augmentation
results = model(img, augment=True)
# parse results
predictions = results.pred[0]
boxes = predictions[:, :4] # x1, x2, y1, y2
scores = predictions[:, 4]
categories = predictions[:, 5]
# show results
results.show()
# save results
results.save(save_dir='results/')
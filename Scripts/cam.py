import os
import cv2
import time
import torch
from PIL import Image
import numpy as np
import pandas

# Model
model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local') 

# init camera
execution_path = os.getcwd()
camera = cv2.VideoCapture(0)

while True:
    # Init and FPS process
    start_time = time.time()

    # Grab a single frame of video
    ret, frame = camera.read()

    # Text
    ftext = "Vison Cork" 

    cv2.putText(frame, ftext, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Inference
    results = model(frame)  # includes NMS

    #results.print()  # print results to screen

    #results.show()  # display results
    #results.save()  # save as results1.jpg, results2.jpg... etc.
    #results.xyxy[0]
    results.pandas().xyxy[0]
   
# Release handle to the webcam
camera.release()
cv2.destroyAllWindows()




       
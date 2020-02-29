#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
     
    # Write your code here for output
    img=cv2.imread('simpsons_frame0.png')

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    out=cv2.inRange(gray,0,6)

    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    
    output=cv2.morphologyEx(out,cv2.MORPH_ERODE,kernel,iterations=3)
    output=cv2.morphologyEx(output,cv2.MORPH_DILATE,kernel,iterations=6)

    output=255-cv2.bitwise_and(output,out)
    
    
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
    
#####################


# In[ ]:





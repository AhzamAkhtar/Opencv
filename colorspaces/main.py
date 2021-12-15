#pip install opencv-contrib-python
#pip install caer
import cv2 as cv
import numpy as np
img=cv.imread("park.jpg")
cv.imshow("park",img)
# 1.converting to gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
# 2. converting gray to hsv
hsv=cv.cvtColor(img,cv.COLOR_RGB2HSV)
cv.imshow("hsv",hsv)
# 3. BGR TO l*b*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)
# 4.BGR TO RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)
#hsv to bgr
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("lab to bgr",lab_bgr)

#color channels bsically splitting imaages into 3 components blue,green,red
b,g,r=cv.split(img)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
# now merging all three components
merged=cv.merge([b,g,r])
cv.imshow("merge image",merged)
# Displaying the Dominating Color in different windows
blank=np.zeros(img.shape[:2],dtype="uint8")
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)
cv.waitKey(0)
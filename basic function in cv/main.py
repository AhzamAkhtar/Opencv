#pip intall opencv-contrib-python
#pip install caer
#notes
import cv2 as cv
import numpy as np
img=cv.imread("park.jpg")
cv.imshow("cat",img)
# Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow("cat_gray",gray)

#Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

#Edge Cascode
canny=cv.Canny(img,200,200) #to found edges
#canny=cv.Canny(blur,200,200) # edges/borders are less in blur photoes
cv.imshow("border",canny)

#Dlitaing the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dilate",dilated)

#Eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow("eroded",eroded)

#Resize image
resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)#cv.INTER_AREA IS USEFUL WHEN YOU ARE SRINKING THE IMAGE
#resize=cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)#USE WHEN SIZE HAS TO BR INCREASED
#resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)#USE WHEN SIZE HAS TO BR INCREASED AND QUALITY IS BETTER THAN cv.LINEAR
cv.imshow("crop_smaller",resize)

#Crop the Image
cropped=img[50:200,200:400]
cv.imshow("croped",cropped)

#IMAGE TRANSFORMATION

#Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
translated=translate(img,100,100)
cv.imshow("translated",translated)
# -x -->Left
# -y --> Up
# +x --> Right
# +y--> Down

# Rotate an Image
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensios=(width,height)
    return cv.warpAffine(img,rotMat,dimensios)
rotated=rotate(img,-45)
cv.imshow("rotated",rotated)
#rotating a rotated image
rotated_rotated=rotate(img,-45)
cv.imshow("Rotated_rotated",rotated_rotated) #adding up the triangles in output

#Flipping the image
flip=cv.flip(img,0)
# flip take only three argument 0,1,-1
# 0 for flipping image vertically over x axis
# 1 for flipping  image horizontally over y axis
# -1 for flipping image in both vertically as well horizontally
cv.imshow("flip",flip)
cv.waitKey(0)
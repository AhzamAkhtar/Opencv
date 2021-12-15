#pip install opencv-contrib-python
import cv2 as cv
import numpy as np
img=cv.imread("cats.jpg")
cv.imshow("cats",img)

#1.Average blurring
average=cv.blur(img,(7,7))
cv.imshow("Average_blur",average)
#2.Gaussian Blur
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian_blur",gauss)
# 3.Median Blur
median=cv.medianBlur(img,7)
cv.imshow("Median_blur",median)
# 4. Bilateral Blurring
bilateral=cv.bilateralFilter(img,5,15,15) #Here 5 is diameter not size of kernal as rest
cv.imshow("bilateral_blurr",bilateral)

#bitwise operation
blank2=np.zeros((400,400),dtype="uint8")
rectangel=cv.rectangle(blank2.copy(),(30,30),(370,370),255,thickness=-1)
circle=cv.circle(blank2.copy(),(200,200),200,255,thickness=-1)
cv.imshow("rectangle",rectangel)
cv.imshow("circle",circle)

#bitwise _and  #SHOWING ONLY COMMAN AREA
bitwise_and=cv.bitwise_and(rectangel,circle)
cv.imshow("bitwise_and",bitwise_and)

#bitwise_or #SHOWING ALL
bitwise_or=cv.bitwise_or(rectangel,circle)
cv.imshow("bitwise_or",bitwise_or)

#bit XOR # showing non intersecting portion
bitwise_xor=cv.bitwise_xor(rectangel,circle)

cv.imshow("bitwise_xor",bitwise_xor)
#bitwise_not #what it does it inverse the color(binary) white to black & black to white(1 to 0& 0 to1)
bitwise_not=cv.bitwise_not(rectangel)
cv.imshow("bitwise_not",bitwise_not)

# Masking
img=cv.imread("cats.jpg")
cv.imshow("cats",img)

blank=np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("blank",blank)
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
#mask=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+100,img.shape[0]//2+100),255,-1)
cv.imshow("Mask",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)
cv.waitKey(0)
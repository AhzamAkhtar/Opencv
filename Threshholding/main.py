import cv2 as cv
import numpy as np
img=cv.imread("cats.jpg")
cv.imshow("cats",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
#simple thresholding
threshold,thresh=cv.threshold(gray,100,250,cv.THRESH_BINARY)
cv.imshow("SIMPLE THRESHOLD",thresh)
# thresh inv
threshold,thresh_inv=cv.threshold(gray,100,250,cv.THRESH_BINARY_INV)
cv.imshow("SIMPLE THRESHOLD Inverse",thresh_inv)

#adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,0)
cv.imshow("adaptive",adaptive_thresh)

#adaptive_inverse thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,0)
cv.imshow("adaptive_inv",adaptive_thresh)

#adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_MEAN,11,0)
#adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_GAUSSIAN,11,0)

#EDGE DETECTION
img2=cv.imread("park.jpg")
cv.imshow("park",img2)

gray=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow("gray_park",gray)

#1.laplocation
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("laplaction",lap)
#2.sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow("sobelx",sobelx)
cv.imshow("sobely",sobely)
cv.imshow("combines",combined_sobel)

#canny
canny=cv.Canny(gray,150,175)
cv.imshow("canny",canny)






cv.waitKey(0)

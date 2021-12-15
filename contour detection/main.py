#pip intall opencv-contrib-python
#pip install caer
#notes
import cv2 as cv
import numpy as np
img=cv.imread("cat.jpg")
cv.imshow("cat",img)
blank=np.zeros(img.shape,dtype="uint8")
cv.imshow("blank",blank)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
'''blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)
canny=cv.Canny(blur,125,175)
cv.imshow("canny",canny)'''
# thresh convert images into binary format 1 or 0 0 for black and 1 for white
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)
contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found!")
# drawing the countours we found into blank
cv.drawContours(blank,contours,-1,(0,0,255),thickness=2) # -1is for index,for drawing all of them write -1
cv.imshow("contours drawn",blank)
cv.waitKey(0)
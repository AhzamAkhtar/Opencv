#pip intall opencv-contrib-python
#pip install caer
#notes
import cv2 as cv
import numpy as np
blank=np.zeros ((500,500,3),dtype="uint8") #creating blan picture
cv.imshow("blank",blank)
#img=cv.imread("cat.jpg")
#cv.imshow("cat",img)
# 1. trying to paint the image with certain colour
#blank[:]=0,255,0 blank[:] means refering all the pixels and setting it to green(255)
#blank[200:300,300:400]=0,255,0
#cv.imshow("green",blank)

#2. draw a recttangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) # TO PAINT RHE WHOLE ARE OF THE BOX
#cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1) # ANOTHER WAY FOR ABOVE
cv.imshow("reactangle",blank)
# 3.Draw Circle
#cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1) #to color the circle
cv.imshow("circle",blank)
# Draw a line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow("line",blank  )

#4 write text
cv.putText(blank,"hello",(210,210),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow("text",blank)
cv.waitKey(0)
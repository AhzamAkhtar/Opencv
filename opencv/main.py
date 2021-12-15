#pip intall opencv-contrib-python
#pip install caer
#notes
#if you have large size images tan it is probably going off screen like cat_large.jpg

#reading images
# you will get -215 error when a vedio ran out of frame or you gave wrong path for a image or vedio
import cv2 as cv
"""img=cv.imread("cat_large.jpg")
cv.imshow("cat",img)
cv.waitKey(0)"""

#reading videos

'''capture=cv.VideoCapture("dog.mp4")
#capture=cv.VideoCapture(0)
#here you can also use your own web cam by replacing "dog.mp4 by 0 int
while True:
    isTrue,frame=capture.read()
    cv.imshow("vedio",frame)
    #to stop the program
    if cv.waitKey(20)==ord("d"): #if letter d is pressed then stop the program
        break
capture.release()
cv.destroyAllWindows()'''

# resizing video and Image
img=cv.imread("cat_large.jpg")
cv.imshow("cat",img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    heigth=int(frame.shape[0]*scale)
    dimension=(width,heigth)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
resized_image=rescaleFrame(img)
cv.imshow("image",resized_image)
capture=cv.VideoCapture("dog.mp4")
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=.2)
    #frame_resized=rescaleFrame(frame)
    cv.imshow("video",frame) # original video
    cv.imshow("video",frame_resized) # resized video
    if cv.waitKey(20)==ord("f"):
        break
capture.release()
cv.destroyAllWindows()
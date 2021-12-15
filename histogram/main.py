import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("cats.jpg")
cv.imshow("cat",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("no of pixles")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)
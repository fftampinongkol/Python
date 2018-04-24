import cv2
import numpy as np

im = cv2.imread('TestIm.jpg')
b,g,r = cv2.split(im)
gr = g-r
blur = cv2.blur(im,(5,5),0)
Gaussblur = cv2.GaussianBlur(im,(7,7),0)
karnel00 = np.array([[1,1,1],[1,1,1],[1,1,1]]) #--- Karnel00 Untuk Lowpass Filter
karnel001 = karnel00*1/16
test0 = cv2.filter2D(gr, -1, karnel001)
karnel01 = np.array([[1,-2,1],[-2,4,-2],[1,-2,1]])
#--- Karnel01 Untuk Highpass Filter karnel01 semua bil.bulat dgn hasil penjumlahan=1
test1 = cv2.filter2D(gr, -1, karnel01)

# print(karnel00)
cv2.imshow("image",im)
# cv2.imshow("blur",blur)
# cv2.imshow("Gauss",Gaussblur)
cv2.imshow("Coba1",test0)
cv2.imshow("Coba2",test1)
# cv2.imshow("Gauss",Gaussblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
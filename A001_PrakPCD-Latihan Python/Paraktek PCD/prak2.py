import cv2
import numpy as np

treshold = 150
image = cv2.imread("bahanprak2.png")
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
row, col, ch = image.shape

treszero = np.zeros((row,col,1), np.uint8)
grayfunct =np.zeros((row,col,1), np.uint8)
grayfunct = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
graykanvas = np.zeros((row,col,1), np.uint8)
#graykanvas[:] = 255
#print image[0,0]
print str(col)+" "+str(row)
print gray[0,0]

              #menghasilkan grayscale

cv2.imshow('image', image)
for i in range(0,row):
    for j in range(0,col):
        blue, green, red = image[i,j]
        gray = red * 0.299 + green * 0.587 + blue * 0.114
        graykanvas.itemset((i,j,0),gray)
        image.itemset((i,j,0),(255-blue))
        image.itemset((i,j,1),(255-green))
        image.itemset((i,j,2),(255-red))

        if gray > treshold:
            treszero.itemset((i,j,0),gray)
        else:
            treszero.itemset((i,j,0),0)


#print image[0,0]

cv2.imshow('grayfunct', grayfunct)
cv2.imshow('invers', image)
cv2.imshow('manual', graykanvas)
cv2.imshow('trest', treszero)

cv2.imwrite('invers.jpg', image)
cv2.imwrite('manual.jpg', graykanvas)
cv2.imwrite('trest.jpg', treszero)

cv2.waitKey(0)
cv2.destroyAllWindows()

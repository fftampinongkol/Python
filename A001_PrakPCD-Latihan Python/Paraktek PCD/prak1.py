import numpy
import cv2

# img = cv2.imread('Datatest03.jpg', 0)
# img1 = cv2.imread('KI_HB_220803901.jpg', -1)
img2 = cv2.imread('Datatest03.jpg')

for n in [0,1000]:
    print(n,1000)

print(img2)
# print(img[0,0])
#
# print('img2')
# print(img2[0,0])

cv2.imshow('Data-1',img2)
cv2.waitKey(0)
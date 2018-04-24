import cv2
import numpy as np
from matplotlib import pyplot as plt
import tools

imgBGR = cv2.imread('KI_HB_220803901.jpg')
# imgGray = cv2.imread('car.png')
# Gray = tools.grayscale(imgGray)

#Histogram GrayScale
# histGray = cv2.calcHist([Gray], [0],
# 							 None, [256], [0, 256])
# plt.hist(Gray.ravel(), 256, [0, 256], label="Gray")
# plt.title("Histogram GrayScale")
# plt.show()

# # Histogram BGR
# color = ('b', 'g', 'r')
# for i, col in enumerate(color):
#     histr = cv2.calcHist([imgBGR], [i], 
#     						None, [256], [0, 256])
#     plt.plot(histr, color=col)
#     plt.xlim([0, 256])
# plt.title("Histogram BGR")
# plt.show()

# Contrast Stretch
stretchy = tools.stretch(imgBGR)
histStret = cv2.calcHist([stretchy], [0], None, [256], [0, 256])
plt.hist(stretchy.ravel(), 256, [0, 256], label="ConStret")
plt.title("Histogram Contrast Stretching")
plt.show()
cv2.imshow("Normal", imgBGR)
cv2.imshow("Stretch", stretchy)
# # Equalize
# equ = cv2.equalizeHist(imgGray)
# histEqu = cv2.calcHist([equ], [0], None, [256], [0, 256])
# plt.hist(equ.ravel(), 256, [0, 256])
# plt.title("Histogram Equalized")
# plt.show()
# cv2.imshow("Original", imgBGR)
# cv2.imshow("Equalized", equ)

# # Histogram Manual
# histo = tools.histogray(Gray)
# cv2.imshow("Histogram", histo)


cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import tools
from matplotlib import pyplot as plt

imRGB = cv2.imread('KI_HB_220803901.jpg')
# gray = tools.grayscale(imRGB)
# cv2.imshow(imRGB, imRGB)
# hisimRGB = cv2.calcHist([imRGB],[0], None, [256], [0,256])
# plt.hist(np.array(),256, [0,256], label="Gray")
# plt.title("Histogram")
# plt.show()

#---- Histogram Color
# color = ('b','g','r')
# for i, col in enumerate(color):
#     hist = cv2.calcHist([imRGB], [i], None, [256], [0,256])
#     plt.plot(hist, color=col)
#     plt.xlim([0,256])
# plt.title("Histogram")
# plt.show()

test = tools.stretch(imRGB)
histest = cv2.calcHist([test], [0], None, [256], [0,256])
plt.hist(test.ravel(), 256, [0,256], label="ConStret")
plt.title("Histogram")
plt.show()
cv2.imshow("Normal", imRGB)
cv2.imshow("stretch", test)

cv2.waitKey(0)
cv2.destroyAllWindows()

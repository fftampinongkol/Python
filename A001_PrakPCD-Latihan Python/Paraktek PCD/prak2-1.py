#--- Praktikum 2 PCD
import cv2

image = cv2.imread("pict.jpg")
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)		#menghasilkan  grayscale

cv2.imwrite('output_gray.jpg', gray)
cv2.imshow('gray_image',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

#--- Mengubah citra menjadi Biner
import cv2

image = cv2.imread("pict.jpg")
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)             	#menghasilkan grayscale
retval, biner = cv2.threshold(gray,50,255, cv2.THRESH_BINARY)   	#menghasilkan citra biner

cv2.imwrite('output_biner.jpg',biner)
cv2.imshow('inibiner', biner)

cv2.waitKey(0)
cv2.destroyAllWindows()

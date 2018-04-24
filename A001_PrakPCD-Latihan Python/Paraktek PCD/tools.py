import cv2
import numpy as np

def grayscale(source):
	row, col, ch = source.shape
	graykanvas = np.zeros((row,col,1), np.uint8)
	for i in range(0,row):
		for j in range(0,col):
			blue, green, red = source[i,j]
			gray = red * 0.299 + green * 0.587 + blue * 0.114
			graykanvas.itemset((i,j,0),gray)
	return graykanvas

def meanImage(source):
	total=0
	row, col, ch = source.shape
	for i in range(0,row):
		for j in range(0,col):
			val = source[i,j]
			total = total + val
			print(total)
	print(total)
	rata = total/(row*col)
	return rata

def treshold (grayimage , tresh):
    row, col , can= grayimage.shape
    output = np.zeros((row,col,1), np.uint8)
    min=max=grayimage[0,0]
    for i in range(0,row):
        for j in range(0,col):
            if grayimage[i,j] > tresh:
                output.itemset((i,j,0), 255)
            else:
                output.itemset((i,j,0), 0)
    return output

def minmax (image):
    row, col= image.shape
    mini=maxi=image[0,0]
    for i in range(0,row):
        for j in range(0,col):
            if image[i,j] < mini:
                mini = image[i,j]
            if image[i,j] > maxi:
                maxi = image[i,j]
    return mini , maxi

def stretch(image):
    row, col , raw= image.shape
    output = np.zeros((row,col,1), np.uint8)
    min=max=image[0,0]
    for i in range(0,row):
        for j in range(0,col):
            if image[i,j] < min:
                min = image[i,j]
            if image[i,j] > max:
                max = image[i,j]
    bawah = max - min
    for i in range(0,row):
        for j in range(0,col):
        	normalize = (float(image[i,j] - min)/bawah)*255
          	output.itemset((i,j,0), normalize)
    return output

def histogray (image):
    buckets = [0] * 300
    arraynorm = [0] * 300
    scale = 1
    histocol= 255
    historow= 150
    border = 30
    kanvashisto = np.zeros(((historow+border),histocol,1), np.uint8)
    row, col , raw = image.shape
    graykanvas = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            buckets[int(image[i,j])]+=1
    maks = max(buckets)
    mins = min(buckets)
    for intent in range(0,255):
        jumlahperbar = buckets[intent]
        normal = int(float(jumlahperbar) / float(maks) * float(historow))
        arraynorm[intent] = normal
        #for x in range(0,scale):
        for y in range(int(historow-normal+border), historow+border):
            kanvashisto.itemset((y, intent, 0) ,255)
    return kanvashisto

# def manHist(img):
#    row, col = img.shape # img is a grayscale image
#    y = np.zeros((256), np.uint64)
#    for i in range(0,row):
#       for j in range(0,col):
#          y[img[i,j]] += 1
#    x = np.arange(0,256)
#    plt.bar(x,y,color="gray",align="center")
#    plt.show()

import cv2
import numpy as np


def median (image, dimensi):

    padd=int(dimensi/2)
    #print padd
    row, col = image.shape
    #print row , col
    kernel = [0] * 10
    output = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            counter = 0
            ancor = i
            ancor2= j
            for k in range((ancor-1),(ancor+2)):
                for l in range((ancor2-1),(ancor2+2)):
                    if(k<0 or l<0 or k>row or l>col):
                        kernel[counter]=0
                        counter= counter+1
                    else:
                        kernel[counter]=image[k-1,l-1]
                        counter= counter+1
                    #print counter


                    #if k>row or l >col:
                    #    return output

            #print counter
            kernel.sort()
            #print kernel
            #print kernel[int((dimensi*dimensi)/2)]
            output.itemset((i,j,0),kernel[int((dimensi*dimensi)/2)])
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
        normal = int(float(jumlahperbar)/float(maks)*float(historow))
        arraynorm[intent] = normal
        #for x in range(0,scale):
        for y in range(int(historow-normal+border), historow+border):
            kanvashisto.itemset((y,intent,0),255)


    return buckets, kanvashisto,arraynorm


def convgray (image):

    row, col , raw = image.shape
    graykanvas = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            blue, green, red = image[i,j]
            gray = red * 0.299 + green * 0.587 + blue * 0.114
            graykanvas.itemset((i,j,0),gray)
    return graykanvas

def minmax (image):
    row, col , raw= image.shape
    min=max=image[0,0]
    for i in range(0,row):
        for j in range(0,col):
            if image[i,j] < min:
                min = image[i,j]
            if image[i,j] > max:
                max = image[i,j]

    return min , max


def stretch (image):
    test= []
    row, col = image.shape
    output = np.zeros((row,col,1), np.uint8)
    mins=image[0,0]
    maxs=image[0,0]
    for i in range(0,row):
        for j in range(0,col):
            if image[i,j] < mins:
                mins = image[i,j]
            if image[i,j] > maxs:
                maxs = image[i,j]
    for i in range(0,row):
        for j in range(0,col):
            normalize = (float(image[i,j]-mins)/(maxs-mins))*255
            output.itemset((i,j,0), normalize)
            #test.append(normalize)
    #print test
    print maxs, mins
    return mins , maxs ,output

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

def negativegray (image):
    row, col , raw= image.shape
    output = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            output.itemset((i,j,0),255-image[i,j])
    return output

def subgraygray (gray1, gray2):
    #catatan ukuran gray 1 dan 2 harus sama dan inten sitas gray2 berupa 0 atau 255 (treshold)
    row, col ,raw = gray2.shape
    output = np.zeros((row,col,1), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if int(gray1[i,j])-int(gray2[i,j]) < 0 :
                output.itemset((i,j,0),0)
            else:
                output.itemset((i,j,0),int(gray1[i,j])-int(gray2[i,j]))
    return output

def subrgbgray(rgb,treshold):
    row, col , raw = rgb.shape
    #print row*col
    output = np.zeros((row,col,3), np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if treshold[i,j] == 255:
                output.itemset((i,j,0),0)
                output.itemset((i,j,1),0)
                output.itemset((i,j,2),0)
            else:
                output[i,j]=rgb[i,j]
    return output
adaw= 100
tester = np.zeros((100,100,1), np.uint8)

for x in range(0,100):
    adaw=adaw+1
    for y in range(0,100):
        tester.itemset((x,y,0),adaw)

#cv2.imshow("aaah", tester)
ganormal = cv2.imread("car.png",0)
ganormalrgb = cv2.imread("car.png")
imageori =cv2.imread("cameraman.jpg",0)
imagergb =cv2.imread("cameraman.jpg")
conv =cv2.imread("conv.jpg",0)


inimin , inimax , outputnih = stretch(ganormal) #fungsi ini melakukan stretching image dan membuat sebaran intensitas menyebar normal
#treshold = treshold(outputnih , 60) # setelah image normal dilakukan tresholding dengan batas treshold '60', dimana nilai yang lebih dari '60' akan manjadi 255 dan dibawah '60' akan menjadi 0.. nilai 60 dapat diubah sesuai kebutuhan
#neg = negativegray(treshold) # fungsi ini mengubah image masukan menjadi negative tapi input image pada fungsi ini harus dalam bentuk grayscale
#subgray= subgraygray(outputnih, neg) # fungsi mengurangkan image gray dengan image gray1
#subrgb = subrgbgray(imagergb,neg) # fungsi mengurangkan image rgb dengan image gray
arrays, histo ,arnorm=histogray(outputnih)
arrays, histo2 ,arnorm2=histogray(convgray(ganormalrgb))
#total=sum(arrays)
#print arrays
#print arnorm
#print total
#print max(arrays)
#print min(arrays)
#outputmed = median(conv,3)
#outputmed = median(outputmed,3)

cv2.imshow("imageorigray", ganormal)
cv2.imshow("hasilstrech", outputnih)
#cv2.imshow("treshold", treshold)
#cv2.imshow("negative", neg)
#cv2.imshow("subgray", subgray)
#cv2.imshow("subrgb", subrgb)
#cv2.imshow("orirgb", imagergb)
#cv2.imshow("magic", outputmed)
cv2.imshow("histogray2", histo2)
cv2.imshow("histogray", histo)


'''
#sukses stretch
inimin2 , inimax2  = minmax(outputnih)
print inimax2 , inimin2
'''
cv2.waitKey(0)
cv2.destroyAllWindows()

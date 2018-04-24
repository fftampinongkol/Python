import pywt
import cv2
import matplotlib.pyplot as plt
import numpy as np

def plotCoeffs(data, outdir):
    rows = len(data)
    cols = len(data[0])

    ##### spectrum ###########
    plt.plot(np.ravel(data))
    plt.title('coeff')
    plt.xlim(0,rows*cols)
    plt.xlabel('Position')
    plt.ylabel('Frequency')
    plt.savefig(outdir+'_coeff.png')
    plt.close()
    plt.close('all')
    plt.gcf().clear()
    ##### Contour ##############
    ax1 = plt.subplot(111)
    ax1.imshow(data, cmap='gray')
    plt.title('dim = '+ str(cols) + 'x' + str(rows))
    plt.savefig(outdir+'_contour.png')
    plt.close()
    plt.close('all')
    plt.gcf().clear()

image= cv2.imread("KI_HB_DSCF7252.jpg")
b,g,r = cv2.split(image)
rg = r-g
coeff = pywt.dwt2(rg,"db3")
LL,(LH,HL,HH) = coeff
print (LL)
plotCoeffs(LL,'ll_b')
plotCoeffs(LH,'lh_b')
plotCoeffs(HL,'hl_b')
plotCoeffs(HH,'hh_b')
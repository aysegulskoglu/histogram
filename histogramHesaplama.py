import cv2
import numpy as np
from matplotlib import pyplot as plt

fotograf = cv2.imread('dag.jpg',0)

hist = np.zeros(256)
[w,h] = np.shape(fotograf)

for v in range (0,h):
    for u in range (0,w):
        i = fotograf[u,v]
        hist[i] = hist[i] + 1

#Degerleri ekrana yazdırır.
for i in range(0,256):
    print(i,"=",hist[i])

cv2.waitKey(0)

histHesapla = cv2.calcHist([fotograf],[0],None,[256],[0,256])
plt.plot(hist, color='#000000')
plt.show()
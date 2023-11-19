import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    gecti,resim = cam.read()   #kameradan görüntüyü alalım.
    hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)  # hsv formatına dönüştürelim.

    lower_red = np.array([0, 100, 100])     #kırmızı renk aralığını belirleyelim.
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(resim, resim,mask = mask)

    cv2.imshow("cam",resim)
    cv2.imshow('Result', result)    

    if cv2.waitKey(1) & 0xFF == ord('q'):  # çıkışı q ile yapalım
        break

cv2.destroyAllWindows()
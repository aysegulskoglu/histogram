#Kütüphanlerimizi ekleyelim
import cv2
import numpy as np

# Görüntümüzü yükleyelim
img = cv2.imread('pirinc.jpg', cv2.IMREAD_COLOR)

# Görüntüyü gri tonlamaya çevirelim
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için blurlayalım
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Kenarları belirleyelim
edges = cv2.Canny(blur, 30, 100)  # Parametreleri değiştirdik

# Kenarları kapalı alanlara dönüştürelim
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtreleme yaparak alanı küçük konturları atlamamızı sağlayalım
min_contour_area = 25
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

# Pirinç tanelerini sayalım
rice_count = len(filtered_contours)

# Sonuçları ekrana yazdıralım
print(f"Pirinç taneleri sayısı: {rice_count}")

# Görüntüyü ekrana çizelim
cv2.drawContours(img, filtered_contours, -1, (0, 255, 0), 2)

# Görüntüyü gösterelim
cv2.imshow('Pirinç Sayımı', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

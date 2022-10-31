import cv2 as cv
import os
path_inicial = os.path.dirname(__file__)
path_foto = os.path.dirname(__file__)

path_foto_cortada = (f"{path_foto}cortada.jpg")

print(path_foto_cortada)

img = cv.imread(f'{path_inicial}\\Fruta.jpg')

height,width = img.shape[:2]


print(height , width)
img2 = cv.resize(img, (800, int( (height * 800) / width) ) )
print(img2)

cv.imwrite(path_inicial + "\\cortada.jpg", img2)
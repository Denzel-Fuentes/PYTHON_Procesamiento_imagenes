import numpy as np
import cv2

capt = cv2.VideoCapture(0)

while True:
    ret, cuadro = capt.read()
    alto, ancho = cuadro.shape[:2]
    center = (ancho / 2, alto / 2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=1, scale=1)
    rotete_image = cv2.warpAffine(cuadro, rotate_matrix, (ancho, alto))
    tiled_image = np.tile(rotete_image, (2, 2, 1)) 
    cv2.imshow('color', tiled_image)
    if cv2.waitKey(1) == ord('q'):
        print('Salida')
        break

capt.release()
cv2.waitKey()
cv2.destroyAllWindows()

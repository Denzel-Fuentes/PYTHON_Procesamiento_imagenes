import numpy as np
import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("image.jpeg")
""" el filtro bilateral  """
blur  = cv2.bilateralFilter(img,30,15,10)

cv2.imshow("original",img)
cv2.imshow("Bilateral",blur)
cv2.waitKey()
cv2.destroyAllWindows()





import numpy as np
import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("flowers.jpg",cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap="gray")
plt.show()
plt.hist(img.flatten(),256)
plt.show()

ret,imgUmbral = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(imgUmbral,cmap="gray")
plt.show()

plt.hist(imgUmbral.flatten(),256)
plt.show()



""" OTSU """
""" cacula el valor del humbral en base al histograma de la imagen """

ret,imgUmbral2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(imgUmbral2,cmap="gray")
plt.show()

plt.hist(imgUmbral2.flatten(),256)
plt.show()


blur  = cv2.GaussianBlur(img,(7,7),0)
plt.imshow(blur,cmap="gray")
plt.show()
plt.hist(blur.flatten(),256)
plt.show()

ret,imgUmbral3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(imgUmbral3,cmap="gray")
plt.show()


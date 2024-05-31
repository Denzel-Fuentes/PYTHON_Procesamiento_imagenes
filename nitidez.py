import numpy as np
import cv2
import matplotlib.pyplot as plt
 
imagen = cv2.imread("flowers.jpeg")
img_color = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
plt.imshow(img_color,cmap="gray")
plt.show()
imagen1 = cv2.GaussianBlur(img_color,(3,3),0)
laplace_red = cv2.Laplacian(imagen1[:,:,0], cv2.CV_64F)
laplace_blue= cv2.Laplacian(imagen1[:,:,1], cv2.CV_64F)
laplace_green= cv2.Laplacian(imagen1[:,:,2], cv2.CV_64F)
plt.imshow(laplace_red)
plt.show()
plt.imshow(laplace_blue)
plt.show()
plt.imshow(laplace_green)
plt.show()
sharp_r = img_color[:,:,0] - 0.7 * laplace_red
sharp_g = img_color[:,:,1] - 0.7 * laplace_green
sharp_b = img_color[:,:,2] - 0.7 * laplace_blue
sharp_r = np.clip(sharp_r, 0, 255).astype(np.uint8)
sharp_g = np.clip(sharp_g, 0, 255).astype(np.uint8)
sharp_b = np.clip(sharp_b, 0, 255).astype(np.uint8)
 
sharp_img = cv2.merge([sharp_r, sharp_g, sharp_b])
plt.imshow(sharp_img)
plt.show()
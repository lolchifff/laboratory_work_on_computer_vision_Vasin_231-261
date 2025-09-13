import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/Users/anifisenko/Documents/laboratory_work_on_computer_vision_Vasin_231-261/src/lab1/pic1.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

r_channel = image_rgb.copy()
g_channel = image_rgb.copy()
b_channel = image_rgb.copy()

r_channel[:, :, 1] = 0 
r_channel[:, :, 2] = 0 

g_channel[:, :, 0] = 0  
g_channel[:, :, 2] = 0 

b_channel[:, :, 0] = 0 
b_channel[:, :, 1] = 0 

plt.subplot(1, 3, 1)
plt.imshow(b_channel)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(g_channel)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(r_channel)
plt.axis('off')

plt.show()
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/Users/anifisenko/Documents/laboratory_work_on_computer_vision_Vasin_231-261/src/lab1/pic1.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Изображение в оттенках серого')
plt.axis('off')  

plt.subplot(1, 2, 2)
plt.imshow(image_rgb)
plt.title('оригинал')
plt.axis('off')  
plt.show()
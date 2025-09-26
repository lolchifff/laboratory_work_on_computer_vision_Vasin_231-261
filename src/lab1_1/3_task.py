import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('src\lab1\pic1.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold_value = 127
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

black_pixels = np.sum(binary_image == 0)
white_pixels = np.sum(binary_image == 255)

ratio = black_pixels / white_pixels if white_pixels != 0 else 0

print(f"Чёрных пикселей: {black_pixels}")
print(f"Белых пикселей: {white_pixels}")
print(f"Соотношение чёрных к белым пикселям: {ratio:.2f}")


plt.figure(figsize=(12, 8))


plt.subplot(3, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Оригинальное изображение')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Бинаризованное изображение')
plt.axis('off')



binary_image_adaptive = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1)

black_pixels_otsu = np.sum(binary_image_adaptive == 0)
white_pixels_otsu = np.sum(binary_image_adaptive == 255)
ratio_otsu = black_pixels_otsu / white_pixels_otsu if white_pixels_otsu != 0 else 0

print(f"Чёрных пикселей (Оцу): {black_pixels_otsu}")
print(f"Белых пикселей (Оцу): {white_pixels_otsu}")
print(f"Соотношение чёрных к белым пикселям (Оцу): {ratio_otsu:.2f}")


plt.subplot(3, 2, 3)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Оригинальное изображение')
plt.axis('off')


plt.subplot(3, 2, 4)
plt.imshow(binary_image_adaptive, cmap='gray')
plt.title('Бинаризация методом адаптивной бинаризации')
plt.axis('off')

plt.show()
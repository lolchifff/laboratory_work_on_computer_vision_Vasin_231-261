import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/Users/anifisenko/Documents/laboratory_work_on_computer_vision_Vasin_231-261/src/lab1/pic1.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, bin_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

thresh = 127
maxval = 255
_, thresh_binary_inv = cv2.threshold(gray_image, thresh, maxval, cv2.THRESH_BINARY_INV)
_, thresh_trunc = cv2.threshold(gray_image, thresh, maxval, cv2.THRESH_TRUNC)
_, thresh_tozero = cv2.threshold(gray_image, thresh, maxval, cv2.THRESH_TOZERO)
_, thresh_tozero_inv = cv2.threshold(gray_image, thresh, maxval, cv2.THRESH_TOZERO_INV)

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Полутоновое изображение (Grayscale)")
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(bin_image, cmap='gray')
plt.title("Бинарное изображение")
plt.axis('off')

plt.subplot(3, 2, 3)
plt.imshow(thresh_binary_inv, cmap='gray')
plt.title("THRESH_BINARY_INV")
plt.axis('off')

plt.subplot(3, 2, 4)
plt.imshow(thresh_trunc, cmap='gray')
plt.title("THRESH_TRUNC")
plt.axis('off')

plt.subplot(3, 2, 5)
plt.imshow(thresh_tozero, cmap='gray')
plt.title("THRESH_TOZERO")
plt.axis('off')

plt.subplot(3, 2, 6)
plt.imshow(thresh_tozero_inv, cmap='gray')
plt.title("THRESH_TOZERO_INV")
plt.axis('off')

plt.tight_layout()
plt.show()
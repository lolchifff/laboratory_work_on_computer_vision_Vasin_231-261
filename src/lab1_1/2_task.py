import cv2
import matplotlib.pyplot as plt


image = cv2.imread('src\lab1\pic1.jpg')


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
image_ycbcr = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
cv2.imwrite('./lab1/pic1_rgb.jpg', cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
cv2.imwrite('./lab1/pic1_hsv.jpg', cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR))
cv2.imwrite('./lab1/pic1_lab.jpg', cv2.cvtColor(image_lab, cv2.COLOR_LAB2BGR))
cv2.imwrite('./lab1/pic1_ycbcr.jpg', cv2.cvtColor(image_ycbcr, cv2.COLOR_YCrCb2BGR))
cv2.imwrite('./lab1/pic1_gray.jpg', image_gray)

    # Отображение изображений для анализа
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

axs[0, 0].imshow(image_rgb)
axs[0, 0].set_title('RGB')
axs[0, 0].axis('off')

axs[0, 1].imshow(image_hsv)
axs[0, 1].set_title('HSV')
axs[0, 1].axis('off')

axs[0, 2].imshow(image_lab)
axs[0, 2].set_title('LAB')
axs[0, 2].axis('off')

axs[1, 0].imshow(image_ycbcr)
axs[1, 0].set_title('YCbCr')
axs[1, 0].axis('off')

axs[1, 1].imshow(image_gray, cmap='gray')
axs[1, 1].set_title('Grayscale')
axs[1, 1].axis('off')

plt.show()

print("Исходное изображение (BGR):")
print(f"Размер изображения: {image.shape}")
print(f"Количество каналов: {image.shape[2]}")
print(f"Тип данных: {image.dtype}")

print("\nRGB изображение:")
print(f"Размер изображения: {image_rgb.shape}")
print(f"Количество каналов: {image_rgb.shape[2]}")
print(f"Тип данных: {image_rgb.dtype}")

print("\nHSV изображение:")
print(f"Размер изображения: {image_hsv.shape}")
print(f"Количество каналов: {image_hsv.shape[2]}")
print(f"Тип данных: {image_hsv.dtype}")

print("\nLAB изображение:")
print(f"Размер изображения: {image_lab.shape}")
print(f"Количество каналов: {image_lab.shape[2]}")
print(f"Тип данных: {image_lab.dtype}")

print("\nYCbCr изображение:")
print(f"Размер изображения: {image_ycbcr.shape}")
print(f"Количество каналов: {image_ycbcr.shape[2]}")
print(f"Тип данных: {image_ycbcr.dtype}")

print("\nGrayscale изображение:")
print(f"Размер изображения: {image_gray.shape}")
print(f"Количество каналов: 1 (только яркость)")
print(f"Тип данных: {image_gray.dtype}")
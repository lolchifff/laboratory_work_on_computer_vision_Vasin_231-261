import cv2
import matplotlib.pyplot as plt

def resize_image(image, width, height):

    resized_image = cv2.resize(image, (width, height))
    return resized_image

def resize_image_aspect_ratio(image, width=None, height=None):
    h, w = image.shape[:2]
    aspect_ratio = w / h
    new_height = int(width / aspect_ratio)
    resized_image = cv2.resize(image, (width, new_height))

    aspect_ratio = h / w
    new_width = int(height / aspect_ratio)
    resized_image = cv2.resize(image, (new_width, height))

    return resized_image


image = cv2.imread('src\lab1\pic1.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h = int(input())
w = int(input())

plt.figure(figsize=(6, 6))

plt.subplot(3, 2, 1)
plt.imshow(resize_image(image, w, h))
plt.title('Оригинальное изображение')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(resize_image_aspect_ratio(image, w, h))
plt.title('Бинаризованное изображение')
plt.axis('off')

plt.show()
import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_white_to_black_area(image, block_size=100, ratio=3):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    height, width = binary_image.shape
    result = []
    for y in range(0, height - block_size, block_size):
        for x in range(0, width - block_size, block_size):
            block = binary_image[y:y + block_size, x:x + block_size]
            white_pixels = np.sum(block == 255)
            black_pixels = np.sum(block == 0)
            if white_pixels >= ratio * black_pixels:
                result.append((x, y))
    return result

image = cv2.imread('src\lab1\pic1.jpg')
areas = find_white_to_black_area(image)

for (x, y) in areas:
    cv2.rectangle(image, (x, y), (x + 100, y + 100), (199, 36, 177), 3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
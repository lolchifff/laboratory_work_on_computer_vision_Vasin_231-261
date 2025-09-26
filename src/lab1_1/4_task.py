import cv2
import matplotlib.pyplot as plt

image = cv2.imread('src\lab1\pic1.jpg')

height, width, _ = image.shape

image_with_border = image.copy()

image_with_border[0, :, :] = [0, 0, 255]
image_with_border[height-1, :, :] = [0, 0, 255]

image_with_border[:, 0, :] = [0, 0, 255]
image_with_border[:, width-1, :] = [0, 0, 255]

cv2.imwrite('src\lab1_1\pic1_with_border.jpg', image_with_border)

fragment = image_with_border[0:30, 0:10]

plt.imshow(cv2.cvtColor(fragment, cv2.COLOR_BGR2RGB))
plt.title("Фрагмент изображения с рамкой")
plt.axis('off')
plt.show()

print("Фрагмент изображения")
print(fragment)
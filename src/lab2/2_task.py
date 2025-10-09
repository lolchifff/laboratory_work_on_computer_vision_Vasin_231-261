from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def apply_filter(image_array, core):
    h, w, c = image_array.shape
    kh, kw = core.shape
    pad_h, pad_w = kh // 2, kw // 2
    
    padded_image = np.pad(image_array, ((pad_h, pad_h), (pad_w, pad_w), (0, 0)), mode='reflect')

    filtered_image = np.zeros_like(image_array)
    for i in range(h):
        for j in range(w):
            for ch in range(c):
                region = padded_image[i:i+kh, j:j+kw, ch]
                filtered_image[i, j, ch] = np.sum(region * core)
    
    return filtered_image.astype(np.uint8)
img = Image.open('src/lab1/pic1.jpg')
img_array = np.array(img)

core_blur = np.ones((5, 5), dtype=np.float32) / 25 
blurred_image = apply_filter(img_array, core_blur)

sharp_kernel_1 = np.array([[ 0, -1,  0], 
                           [-1,  5, -1], 
                           [ 0, -1,  0]], dtype=np.float32)


sharp_kernel_2 = np.array([[-2, -2, -1], 
                           [-1,  9, -1], 
                           [-1, -2, -2]], dtype=np.float32)


sharp_image_1 = apply_filter(blurred_image, sharp_kernel_1)
sharp_image_2 = apply_filter(blurred_image, sharp_kernel_2)

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(img_array)
plt.title('Исходное изображение')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(blurred_image)
plt.title('Размытие (усредняющий фильтр)')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(sharp_image_1)
plt.title('Повышение резкости (стандартное ядро)')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(sharp_image_2)
plt.title('Повышение резкости (агрессивное ядро)')
plt.axis('off')

plt.show()
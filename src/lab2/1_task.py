from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt 
img = Image.open('src\lab1\pic1.jpg')
img_array = np.array(img)


noise = np.random.normal(0, 25, img_array.shape).astype(np.int16)
noisy = img_array + noise
noisy = np.clip(noisy, 0, 255).astype(np.uint8) 

core = np.ones((5,5), dtype=np.float32 ) / 25


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

filtered = apply_filter(noisy, core)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(noisy)
plt.title('Изображение с шумом')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(filtered)
plt.title('После усредняющего фильтра 5×5')
plt.axis('off')
plt.show()
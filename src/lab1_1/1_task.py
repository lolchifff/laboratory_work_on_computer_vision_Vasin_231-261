    import cv2
    import matplotlib.pyplot as plt


    image = cv2.imread('src\lab1\pic1.jpg')
    image_shape = image.shape
    image_size = image.size
    image_dtype = image.dtype
    image_channels = image.shape[2] if len(image.shape) > 2 else 1 
    color_space = "BGR" if image_channels == 3 else "Grayscale"

    print(f"Размер изображения: {image_shape}\nОбщее количество пикселей: {image_size}\nТип данных: {image_dtype}\nЦветовое пространство: {color_space}")


    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()

    cv2.imwrite('src\lab1_1\pic1_rgb.jpg',image_rgb)
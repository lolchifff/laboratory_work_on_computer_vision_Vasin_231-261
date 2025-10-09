import cv2
import numpy as np

def count_holes(image_path: str):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, bin_img = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(bin_img, connectivity=8)

    h, w = bin_img.shape
    holes_count = 0

    for label in range(1, num_labels):
        x, y, w_, h_, area = stats[label]
        if x <= 0 or y <= 0 or x + w_ >= w - 1 or y + h_ >= h - 1:
            continue
        holes_count += 1

    return holes_count

if __name__ == "__main__":
    holes_1_test = count_holes('src/lab2/test1.png')
    holes_2_test = count_holes('src/lab2/test2.png')
    holes_3_test = count_holes('src/lab2/test3.png')
    holes_4_test = count_holes('src/lab2/test4.png')
    holes_5_test = count_holes('src/lab2/test5.png')
    print(holes_1_test)
    print(holes_2_test)
    print(holes_3_test)
    print(holes_4_test)
    print(holes_5_test)

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('/Users/anifisenko/Documents/laboratory_work_on_computer_vision_Vasin_231-261/src/lab1/pic1.jpg')
img2 = cv2.imread('/Users/anifisenko/Documents/laboratory_work_on_computer_vision_Vasin_231-261/src/lab1/pic2.jpg')


img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

r_channel_img1 = img1_rgb.copy()
g_channel_img1 = img1_rgb.copy()
b_channel_img1 = img1_rgb.copy()

r_channel_img2 = img2_rgb.copy()
g_channel_img2 = img2_rgb.copy()
b_channel_img2 = img2_rgb.copy()



r_channel_img1[:, :, 1] = 0 
r_channel_img1[:, :, 2] = 0 

g_channel_img1[:, :, 0] = 0  
g_channel_img1[:, :, 2] = 0 

b_channel_img1[:, :, 0] = 0 
b_channel_img1[:, :, 1] = 0 



r_channel_img2[:, :, 1] = 0 
r_channel_img2[:, :, 2] = 0 

g_channel_img2[:, :, 0] = 0  
g_channel_img2[:, :, 2] = 0 

b_channel_img2[:, :, 0] = 0 
b_channel_img2[:, :, 1] = 0 


r_added = cv2.add(r_channel_img1, r_channel_img2)
g_added = cv2.add(g_channel_img1, g_channel_img2)
b_added = cv2.add(b_channel_img1, b_channel_img2)

r_result = r_added[:, :, 0]
g_result = g_added[:, :, 1] 
b_result = b_added[:, :, 2]


sum_image = cv2.merge([r_result, g_result, b_result])



r_razn = cv2.subtract(r_channel_img1, r_channel_img2)
g_razn = cv2.subtract(g_channel_img1, g_channel_img2)
b_razn = cv2.subtract(b_channel_img1, b_channel_img2)

r_razn_channel = r_razn[:, :, 0]  
g_razn_channel = g_razn[:, :, 1]  
b_razn_channel = b_razn[:, :, 2]

result_subtracted = cv2.merge([r_razn_channel, g_razn_channel, b_razn_channel])

plt.subplot(1, 2, 1)
plt.imshow(sum_image)
plt.title('Поканальное сложение')
plt.axis('off') 

plt.subplot(1, 2, 2)
plt.imshow(result_subtracted)
plt.title('Поканальное вычитание')
plt.axis('off')

plt.tight_layout()
plt.show()
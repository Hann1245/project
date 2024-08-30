import numpy as np
import cv2

# Đọc ảnh từ file
image = cv2.imread('D:/ccjdo/pythonProject/img/cheems4.jpg')
# nhập cường độ sáng tối muốn tăng/giảm
increase_brightness = int(input('Tăng độ sáng: '))
decrease_brightness = int(input('Giảm độ sáng: '))

# Tăng độ sáng bằng cách cộng thêm một giá trị vào từng pixel
bright_image = np.clip(image + increase_brightness, 0, 255)

# Giảm độ sáng bằng cách trừ đi một giá trị từ từng pixel
dark_image = np.clip(image - decrease_brightness, 0, 255)

# showww
cv2.imshow('bright_image', bright_image)
cv2.imshow('dark_image', dark_image)
cv2.waitKey(0)

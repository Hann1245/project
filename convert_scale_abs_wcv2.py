import cv2

# đọc ảnh
image = cv2.imread('D:/ccjdo/pythonProject/img/cheems4.jpg')
#nhập giá trị beta để tăng giảm độ sáng
increase_brightness = int(input('Tăng độ sáng: '))
decrease_brightness = int(input('Giảm độ sáng: '))

# điều chỉnh độ sáng
bright_image = cv2.convertScaleAbs(image, alpha=1, beta=increase_brightness)  # tăng độ sáng
dark_image = cv2.convertScaleAbs(image, alpha=1, beta=-decrease_brightness)   # giảm độ sáng

# show
cv2.imshow('bright_image.jpg', bright_image)
cv2.imshow('dark_image.jpg', dark_image)
cv2.waitKey(0)
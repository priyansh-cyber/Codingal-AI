import cv2 
import matplotlib.pyplot as plt
image_path = "image.jpg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 225, 225), 3)
plt.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title("annotated image with regions, centers, and bi-directional height arrow")
plt.axis("off")
plt.show()
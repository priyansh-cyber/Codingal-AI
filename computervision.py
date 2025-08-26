import cv2
print(cv2.__version__)
image=cv2.imread("image.jpg")

cv2.imshow("my image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
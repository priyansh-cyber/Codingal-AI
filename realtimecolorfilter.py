import cv2
import numpy as np
def apply_color_filter(image, filter_type):
    """apply the specified ocolor filter to the imgae"""
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype("unit8"), sobely.astype("unit8"))
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
       gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
       edges = cv2.Canny(gray_image, 100, 200)
       filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return filtered_image

image_path = "fire spritew.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("error: image not found")
else:
    filter_type = "orignal"

    print("press the following keys to applt the filter")
    print("r - red tint")
    print("b - blue tint")
    print("g - green tint")
    print("s - sobel edge detection")
    print("c - canny edg detection")
    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("filtered image", filtered_image)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("r"):
            filter_type = "red_tint"
        elif key == ord("b"):
            filter_type = "blue tint"
        elif key == ord("g"):
            filter_type = "green tint"
        elif key == ord("s"):
            filter_type = "sobel"
        elif key == ord("c"):
            filter_type = "canny"
            break
        else:
            print("invalid key! please use r, b, g, s, c")

    cv2.destroyAllWindows

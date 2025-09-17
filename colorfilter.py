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
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    return filtered_image

image_path = "images.jpg"
image = cv2.imread(image_path)

if image is None:
    print("error: image not found")
else:
    filter_type = "orignal"

    print("press the following keys to applt the filter")
    print("r - red tint")
    print("b - blue tint")
    print("g - green tint")
    print("i - increase red intesity")
    print("d - increase blue intesity")
    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("filtered image", filtered_image)
        key = cv2.waitkey(0) & 0xFF
        if key == ord("r"):
            filter_type = "red_tint"
        elif key == ord("b"):
            filter_type = "blue tint"
        elif key == ord("g"):
            filter_type = "green tint"
        elif key == ord("i"):
            filter_type = "increase red intesity"
        elif key == ord("d"):
            filter_type = "increase blue intesity"
            break
        else:
            print("invalid key! please use r, b, g, i, d")

    cv2.destroyAllWindows

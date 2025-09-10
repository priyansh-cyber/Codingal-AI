import cv2 
import numpy as np 
import matplotlib.pyplot as plt
def desply_image(title, image):
    """utility function to display an image"""
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2: 
        plt.imshow(image, cmap="gray")
    else:
        plt.ismshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def interactive_edge_detection(image_path):
    """interactive activity for edge dection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print("error: image not found")
        return
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    desply_image("orignal grayscale image", gray_image)

    print("select an option")
    print("1. sobel edge detection")
    print("2. canny edge detection")
    print("3. lapacian edge detection ")
    print("4. gaussain smooting")
    print("5. median filtering")
    print("6. exit")
    while True:
        choice = input("enter you choice(1-6):")
        if choice == "1":
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            desply_image("sobel edge detion", combined_sobel )
        elif choice == "2":
            print("adjust threshold for cranny(default: 100 and 200)")
            lower_thresh = int(input("enter lower threshold"))
            upper_thresh = int(input("enter upper threshold"))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            desply_image("canny edge detion", edges )
        elif choice == "3":
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            desply_image("Laplacian edge detion", np.abs(laplacian).astype(np.uint8) )
        elif choice == "4":
            print("adjust kernel size for gaussian blur (must be odd, default:5)")
            kernel_size = int(input("enter kernel size(oddnumber):"))
            blured = cv2.GaussianBlur(image,(kernel_size, kernel_size), 0)
            desply_image("gaussian edge detion", blured)
        elif choice =="5":
            print("adjust kernel size for median filtering (must be odd, default:5)")
            kernel_size = int(input("enter kernel size(oddnumber):"))
            median_filtered = cv2.medianBlur(image,(kernel_size, kernel_size), 0)
            desply_image("gaussian edge detion", median_filtered)
        elif choice == "6":
            print("exiting..")
            break
        else:
            print("invalid choice. please select correct")

interactive_edge_detection("example.jpg")
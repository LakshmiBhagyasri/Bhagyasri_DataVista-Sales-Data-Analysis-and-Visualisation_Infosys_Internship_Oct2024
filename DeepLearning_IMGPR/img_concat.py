import cv2
import numpy as np
import os

# Paths to the images
img1_path = 'C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/image1.jpeg'
img2_path = 'C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/image2.jpeg'

# Load images
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

# Check if the images were loaded correctly
if img1 is None:
    print(f"Error: Couldn't load the image at {img1_path}. Please check the file path.")
elif img2 is None:
    print(f"Error: Couldn't load the image at {img2_path}. Please check the file path.")
else:
    # Resize images to the same dimensions
    img1 = cv2.resize(img1, (500, 500))
    img2 = cv2.resize(img2, (500, 500))  

    # Concatenate images horizontally and vertically
    h_concat = np.hstack((img1, img2))
    v_concat = np.vstack((img1, img2))

    # Display the concatenated images
    cv2.imshow('Horizontal Concatenation', h_concat)
    cv2.imshow('Vertical Concatenation', v_concat)

    # Wait for any key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

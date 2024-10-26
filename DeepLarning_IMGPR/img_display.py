import os
import cv2

# Path to the folder containing JPEG images (using a raw string)
folder_path = 'C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/task-1'

# Get list of all JPEG image files in the folder
jpeg_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg'))]

# Loop to load and read JPEG images
for img_file in jpeg_files:
    img_path = os.path.join(folder_path, img_file)
    img = cv2.imread(img_path)
    
    # Check if the image was loaded successfully
    if img is not None:
        # Display each image (optional)
        cv2.imshow(f'JPEG Image: {img_file}', img)
        cv2.waitKey(0)  # Press any key to close the image window
    else:
        print(f'Failed to load image: {img_path}')

cv2.destroyAllWindows()

